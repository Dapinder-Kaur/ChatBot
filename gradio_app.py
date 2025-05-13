import gradio as gr
import random
import time
from google import genai
import os
from dotenv import load_dotenv
from google.genai import types
from chatbot import *


# Load environment variables
load_dotenv()

client = genai.Client(api_key=os.environ.get("API_KEY"))


# with gr.Blocks() as demo:
#     history_for_gemini = []
#     chatbot = gr.Chatbot(type="messages")
#     msg = gr.Textbox()
#     clear = gr.ClearButton([msg, chatbot])

#     def respond(message, chat_history):
#         global history_for_gemini
#         history_for_gemini = history_function(history_for_gemini, "user", message)
#         response = client.models.generate_content(
#             model="gemini-2.0-flash",
#             contents=history_for_gemini,
#             config=generate_content_config,
#         )
#         history_for_gemini = history_function(
#             history_for_gemini, "model", response.text
#         )
#         chat_history.append({"role": "user", "content": message})
#         chat_history.append({"role": "assistant", "content": response.text})

#         return "", chat_history

#     msg.submit(fn=respond, inputs=[msg, chatbot], outputs=[msg, chatbot])
#     # clear.click(lambda: None, None, chatbot, queue=False)

# demo.launch()


with gr.Blocks() as demo:
    history_for_gemini = []
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    def user(user_message, history: list):
        global history_for_gemini
        history_for_gemini = history_function(history_for_gemini, "user", user_message)
        return "", history + [{"role": "user", "content": user_message}]

    def bot(history: list):
        global history_for_gemini

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=history_for_gemini,
            config=generate_content_config,
        )
        history_for_gemini = history_function(
            history_for_gemini, "model", response.text
        )
        history.append({"role": "assistant", "content": ""})
        for character in response.text:
            history[-1]["content"] += character
            # time.sleep(0.05)
            yield history

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch()
