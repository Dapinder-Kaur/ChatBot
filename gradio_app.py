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
history_gradio = []


# def chatbot_interface(user_input):
#     global history
#     global history_gradio

#     history.append(
#         types.Content(role="user", parts=[types.Part.from_text(text=user_input)])
#     )
#     history_gradio.append({"role": "user", "content": user_input})

#     response = response_system_prompt(history)

#     chunk_response = "".join(chunk.text for chunk in response)

#     history = chat_history_function(user_input, chunk_response)

#     chunk_response_gradio = ""

#     for chunk in response:
#         chunk_response_gradio += chunk.text
#         yield history_gradio + [{"role": "assistant", "content": chunk_response_gradio}]

#     history_gradio.append({"role": "assistant", "content": chunk_response_gradio})
#     return [
#         {"role": "user", "content": user_input},
#         {"role": "assistant", "content": chunk_response},
#     ]


# with gr.Blocks() as demo:
#     chatbot = gr.Chatbot(label="Chatbot", type="messages")
#     msg = gr.Textbox()
#     clear = gr.ClearButton([msg, chatbot])

#     msg.submit(chatbot_interface, inputs=msg, outputs=chatbot)

# demo.launch()

import gradio as gr
import random
import time

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=message,
        )
        chat_history.append({"role": "user", "content": message + "lol"})
        chat_history.append({"role": "assistant", "content": response.text})
        return "", chat_history

    msg.submit(fn=respond, inputs=[msg, chatbot], outputs=[msg, chatbot])

demo.launch()
