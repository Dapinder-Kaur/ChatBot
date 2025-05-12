from google import genai
from PIL import Image
import time
import streamlit as st
import os
from chatbot import (
    chatbot_stream_response,
    chat_history_function,
    response_system_prompt,
    history_function,
)
import sys
from dotenv import load_dotenv
from google.genai import types


load_dotenv()


client = genai.Client(
    api_key=os.environ.get("API_KEY"),
)


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


def main():
    chat_history: list[types.Content] = []

    try:
        while True:
            input_text = input(f"{Yellow}User: {Reset}")
            chat_history = history_function(chat_history, "user", input_text)
            response = response_system_prompt(chat_history)
            print(f"{Blue}ChatBot: {Reset}", end="")
            chunk_response = ""

            for chunk in response:
                print(chunk.text, end="")
                chunk_response += chunk.text

            chat_history = history_function(chat_history, "model", chunk_response)

    except KeyboardInterrupt:
        print(f"\n{Red}Exiting...{Reset}")
        sys.exit(0)


if __name__ == "__main__":
    main()
