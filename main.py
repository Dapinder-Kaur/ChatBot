from google import genai
from PIL import Image
import time
import streamlit as st
import os
from chatbot import (
    chatbot_stream_response,
    chat_history_function,
    response_system_prompt,
)
import sys
from dotenv import load_dotenv
from google.genai import types


# loading the environment variables from the .env file
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
    history = []

    try:
        while True:
            # to take an input from the user
            def input_text():
                return input(f"{Yellow}User: {Reset}")

            input_text = input_text()

            # storing the gemini's response

            history.append(
                types.Content(
                    role="user", parts=[types.Part.from_text(text=input_text)]
                )
            )

            response = response_system_prompt(history)

            print(f"{Blue}Gemini: {Reset}", end="")

            chunk_response = ""

            for chunk in response:
                print(chunk.text, end="")
                chunk_response += chunk.text

            history = chat_history_function(input_text, chunk_response)

    except KeyboardInterrupt:

        print(f"\n{Red}Exiting...{Reset}")
        sys.exit(0)
        # zero here represents the successful termination of the program


if __name__ == "__main__":
    main()
