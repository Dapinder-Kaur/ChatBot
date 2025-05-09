# importing the required libraries
from google import genai
from PIL import Image
import time
import streamlit as st
import os
from chatbot import chatbot_stream_response
import sys

# API_KEY = "AIzaSyCRL3Ujbp6j-Gh1d1kO3PNWBLJqc5a1QGU"
# setting up the client with the API key
client = genai.Client(
    api_key=os.environ.get("API_KEY"),
)


system_prompt = "Your name is Baxter, and you are a personal assistant at TACAM, whose job is to give the tours\
    in the smart factory. You are a polite and helpful communicator at \
    Red River College Polytechnic providing quality of service. We have a robot playing chess, its white in color and has a screen.\
        Smart Factory is located in T building at Red River College Polytechnic"

chat_history = []
formatted_history = []
prompt_template = (
    "System: {system_prompt} \nHistory: {chat_history} \nUser: {user_input}"
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


# for streamlit
def input_text():
    return input(f"{Yellow}User: {Reset}")


def main():
    # an example_usage function to test the API
    def example_usage():
        response = client.models.generate_content_stream(
            model="gemini-2.0-flash", contents="Hi, How are you?"
        )
        return response

    try:
        while True:
            # to take an input from the user
            def input_text():
                return input(f"{Yellow}User: {Reset}")

            input_text = input_text()
            chat_history.append({"user": input_text})
            formatted_history = "\n".join(
                [f"User: {msg['user']}" for msg in chat_history]
            )

            final_prompt = prompt_template.format(
                system_prompt=system_prompt,
                chat_history=formatted_history,
                user_input=input_text,
            )
            # storing the gemini's response

            response = chatbot_stream_response(final_prompt)

            # response = example_usage() # to test the example_usage function

            # printing the response in chunks
            print(f"{Blue}Gemini: {Reset}", end="")
            for chunk in response:
                print(chunk.text, end="")

    except KeyboardInterrupt:
        print(f"\n{Red}Exiting...{Reset}")
        sys.exit(0)
        # zero here represents the successful termination of the program


if __name__ == "__main__":
    main()
