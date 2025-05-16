import gradio as gr
import random
import time
from google import genai
import os
from dotenv import load_dotenv
from google.genai import types
from chatbot_functions import *


# Load environment variables
load_dotenv()

client = genai.Client(api_key=os.environ.get("API_KEY"))
history_for_gemini = []

system_prompt_value = """Your name is Baxter, and you are a personal assistant at TACAM, whose job is to give the tours in the smart factory. 
You are a polite and helpful communicator at Red River College Polytechnic providing quality of service. 
We have a robot playing chess, its white in color and has a screen.
Smart Factory is located in T building at Red River College Polytechnic.
Respond only in single sentence.
If user's input is blank, ask to repeat again saying that you did not understand."""


def user(user_message: str, history: list):
    global history_for_gemini
    history_for_gemini = history_function(history_for_gemini, "user", user_message)
    return "", history + [{"role": "user", "content": user_message}]


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


with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    msg_textbox = gr.Textbox()
    clear_button = gr.Button("Clear")
    with gr.Accordion("This is your system prompt", open=False):
        system_prompt_textbox = gr.Textbox(
            label="Enter your system prompt here ...",
            value=system_prompt_value,
            lines=5,
        )

    msg_textbox.submit(
        user, [msg_textbox, chatbot], [msg_textbox, chatbot], queue=False
    ).then(bot, [chatbot, system_prompt_textbox], chatbot)
    clear_button.click(lambda: None, None, chatbot, queue=False)

demo.launch()
