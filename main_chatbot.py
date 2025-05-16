from google import genai
from PIL import Image
import time
import streamlit as st
import os
import chatbot_functions as cb
import sys
from google.genai import types


client = cb.client


def main():
    chat_history: list[types.Content] = []

    try:
        while True:
            input_text = input(f"{cb.Yellow}User: {cb.Reset}")
            chat_history = cb.history_function(chat_history, "user", input_text)
            response = cb.response_system_prompt(chat_history)
            print(f"{cb.Blue}ChatBot: {cb.Reset}", end="")
            chunk_response = ""

            for chunk in response:
                print(chunk.text, end="")
                chunk_response += chunk.text

            chat_history = cb.history_function(chat_history, "model", chunk_response)

    except KeyboardInterrupt:
        print(f"\n{cb.Red}Exiting...{cb.Reset}")
        sys.exit(0)


if __name__ == "__main__":
    main()
