import gradio as gr
import random
import time
from google import genai
import os
from dotenv import load_dotenv
from google.genai import types
from chatbot import (
    chatbot_stream_response,
    chat_history_function,
    response_system_prompt,
)


# Load environment variables
load_dotenv()

client = genai.Client(api_key=os.environ.get("API_KEY"))

# Chatbot function for Gradio
history = []


def chatbot_interface(user_input):
    global history

    history.append(
        types.Content(role="user", parts=[types.Part.from_text(text=user_input)])
    )

    response = response_system_prompt(history)

    chunk_response = "".join(chunk.text for chunk in response)

    history = chat_history_function(user_input, chunk_response)

    return [
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": chunk_response},
    ]


with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    msg.submit(chatbot_interface, inputs=msg, outputs=chatbot)

demo.launch()
