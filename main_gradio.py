import gradio as gr
from google import genai

from google.genai import types
import chatbot as cb


client = cb.client
history_for_gemini = []

system_prompt_value = cb.system_prompt_textbox


def user(user_message: str, history: list):
    global history_for_gemini
    history_for_gemini = cb.history_function(history_for_gemini, "user", user_message)
    return "", history + [{"role": "user", "content": user_message}]


def bot(history: list, prompt):
    global history_for_gemini

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=history_for_gemini,
        config=cb.generate_content_config_gemini(prompt),
    )
    history_for_gemini = cb.history_function(history_for_gemini, "model", response.text)
    history.append({"role": "assistant", "content": ""})
    for character in response.text:
        history[-1]["content"] += character
        # time.sleep(0.05)
        yield history


with gr.Blocks() as demo:
    # chatbot = gr.Chatbot(type="messages")
    chatbot = gr.Chatbot(elem_id="chatbot")
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
