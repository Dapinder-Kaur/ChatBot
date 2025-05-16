"""A file containing all the important functions needed for chatbot's smooth functionality"""

from typing import Literal
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

# ANSI escape sequences for colored text
Reset = "\033[0m"
Red = "\033[31m"
Green = "\033[32m"
Yellow = "\033[33m"
Blue = "\033[34m"
Magenta = "\033[35m"
Cyan = "\033[36m"
Gray = "\033[37m"
White = "\033[97m"


# setting up the client with the API key
client = genai.Client(
    api_key=os.environ.get("API_KEY"),
)

system_prompt_textbox = """Your name is Baxter, and you are a personal assistant at TACAM, whose job is to give the tours in the smart factory. 
You are a polite and helpful communicator at Red River College Polytechnic providing quality of service. 
We have a robot playing chess, its white in color and has a screen.
Smart Factory is located in T building at Red River College Polytechnic.
Respond only in single sentence.
If user's input is blank, ask to repeat again saying that you did not understand."""


# Function to get chatbot response
def chatbot_response(input_text):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=input_text,
    )
    return response.text


def chatbot_stream_response(input_text):
    response = client.models.generate_content_stream(
        model="gemini-2.0-flash",
        contents=input_text,
    )
    return response


def output_function(response):

    return response


def chat_output(response):
    print(f"{Blue}Gemini: {Reset}", end="")
    for chunk in response:
        # time.sleep(0.1)
        print(chunk.text, end=" ")


# A varable to store the system prompt for the chatbot
generate_content_config = types.GenerateContentConfig(
    response_mime_type="text/plain",
    system_instruction=[types.Part.from_text(text=system_prompt_textbox)],
)


def generate_content_config_gemini(system_prompt: str):
    if system_prompt == "":
        system_prompt = system_prompt_textbox
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text=system_prompt),
        ],
    )
    return generate_content_config


def response_system_prompt(prompt):
    response = client.models.generate_content_stream(
        model="gemini-2.0-flash",
        contents=prompt,
        config=generate_content_config,
    )

    return response


def response_system_prompt_without_streaming(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config=generate_content_config,
    )

    return response.text


# an actual chatbot function
def chatbot_actual(input_text):
    response = client.models.generate_content_stream(
        model="gemini-2.0-flash",
        contents=input_text,
    )

    return response


# a chatbot function for streamlit
def chatbot_actual_for_streamlit(input_text):
    response = client.models.generate_content_stream(
        model="gemini-2.0-flash",
        contents=input_text,
    )

    return response


def example_usage():
    response = client.models.generate_content_stream(
        model="gemini-2.0-flash", contents="Hi, How are you?"
    )

    return response


def chat_history_function(chat_history, input_text, response):

    chat_history.append(
        types.Content(role="user", parts=[types.Part.from_text(text=input_text)])
    )
    chat_history.append(
        types.Content(role="model", parts=[types.Part.from_text(text=response)])
    )
    return chat_history


def input_text():
    return input(f"{Yellow}User: {Reset}")


def history_function(
    chat_history: list[types.Content],
    role: Literal["user"] | Literal["model"],
    text: str,
):
    chat_history.append(
        types.Content(role=role, parts=[types.Part.from_text(text=text)])
    )
    return chat_history
