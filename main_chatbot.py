from google import genai
from PIL import Image
import time
import streamlit as st
import os
import chatbot_functions as cb
import sys
from google.genai import types


client = cb.client


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
            chat_history = cb.history_function(chat_history, "user", input_text)
            response = cb.response_system_prompt(chat_history)
            print(f"{Blue}ChatBot: {Reset}", end="")
            chunk_response = ""

            for chunk in response:
                print(chunk.text, end="")
                chunk_response += chunk.text

            chat_history = cb.history_function(chat_history, "model", chunk_response)

    except KeyboardInterrupt:
        print(f"\n{Red}Exiting...{Reset}")
        sys.exit(0)


if __name__ == "__main__":
    main()
