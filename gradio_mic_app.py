import gradio as gr
import random
import time
from google import genai
import os
from dotenv import load_dotenv
from google.genai import types
from chatbot import generate_content_config_gemini, history_function
from speech_to_text import actual_response_function_for_gradio
from pydub.playback import play
from gtts import gTTS
from pydub import AudioSegment
import speech_recognition as sr


# Load environment variables
load_dotenv()

client = genai.Client(api_key=os.environ.get("API_KEY"))
history_for_gemini = []

system_prompt_value = """Your name is Baxter, and you are a personal assistant at TACAM, whose job is to give the tours in the smart factory. 
You are a polite and helpful communicator at Red River College Polytechnic providing quality of service. 
We have a robot playing chess, its white in color and has a screen.
Smart Factory is located in T building at Red River College Polytechnic.
Respond only in single sentence."""


def audio_to_text(audio_file_path):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"


def process_audio(history, audio):
    global history_for_gemini
    if audio is None:
        return "No audio recorded"

    text = audio_to_text(audio)
    history.append({"role": "user", "content": text})
    history_for_gemini = history_function(history_for_gemini, "user", text)
    return history, gr.Audio(value=None, interactive=False)


def add_message(history, message):
    global history_for_gemini
    # for x in message["files"]:
    #     history.append({"role": "user", "content": {"path": x}})
    #     temp_list = message["files"]
    #     within_list = temp_list[0]["path"]
    #     text = actual_response_function_for_gradio(within_list)
    #     history_for_gemini = history_function(history_for_gemini, "user", text)
    # if message["text"] is not None:
    #     history.append({"role": "user", "content": message["text"]})
    #     history_for_gemini = history_function(
    #         history_for_gemini, "user", message["text"]
    #     )
    history.append({"role": "user", "content": message})
    history_for_gemini = history_function(history_for_gemini, "user", message)

    return history, gr.Textbox(value=None, interactive=False)


def bot(history: list, prompt):
    global history_for_gemini
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=history_for_gemini,
        config=generate_content_config_gemini(prompt),
    )
    history_for_gemini = history_function(history_for_gemini, "model", response.text)
    history.append({"role": "assistant", "content": ""})
    for character in response.text:
        history[-1]["content"] += character
        # time.sleep(0.05)
        yield history

    response = gTTS(response.text)
    response.save("response.mp3")
    chatbot_response = AudioSegment.from_mp3("response.mp3")
    play(chatbot_response)


with gr.Blocks() as demo:
    chatbot = gr.Chatbot(elem_id="chatbot", type="messages")

    # chat_input = gr.MultimodalTextbox(
    #     interactive=True,
    #     file_count="single",
    #     placeholder="Enter message or upload an audio file...",
    #     show_label=False,
    #     sources=["microphone", "upload"],
    # )
    chat_input = gr.Textbox()
    with gr.Row():
        audio_input = gr.Audio(sources=["microphone"], type="filepath")
        audio_button = gr.Button("Submit")
    with gr.Accordion("This is your system prompt", open=False):
        system_prompt_textbox = gr.Textbox(
            label="Enter your system prompt here ...",
            value=system_prompt_value,
            lines=5,
        )

    chat_msg = chat_input.submit(
        add_message, [chatbot, chat_input], [chatbot, chat_input]
    )
    # audio_msg = chat_msg.then(process_audio, [chatbot, audio_input], chatbot)

    bot_msg = chat_msg.then(
        bot, [chatbot, system_prompt_textbox], chatbot, api_name="bot_response"
    )
    bot_msg.then(lambda: gr.Textbox(interactive=True), None, [chat_input])

    audio_button.click(
        process_audio, [chatbot, audio_input], [chatbot, audio_input]
    ).then(lambda: None, inputs=None, outputs=audio_input).then(
        bot, [chatbot, system_prompt_textbox], chatbot, api_name="bot_response"
    ).then(
        lambda: gr.Audio(interactive=True), None, [audio_input]
    )

demo.launch()
