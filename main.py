# importing the required libraries
from google import genai
from PIL import Image
import time
import streamlit as st


# setting up the client with the API key
client = genai.Client(api_key="AIzaSyCRL3Ujbp6j-Gh1d1kO3PNWBLJqc5a1QGU")


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
    # an example_usage function to test the API
    def example_usage():
        response = client.models.generate_content_stream(
            model="gemini-2.0-flash", contents="Hi, How are you?"
        )
        return response

    # an actual chatbot function
    def chatbot_actual(input_text):
        response = client.models.generate_content_stream(
            model="gemini-2.0-flash",
            contents=input_text,
        )

        return response

    # to take an input from the user
    def input_text():
        return input(f"{Yellow}User: {Reset}")

    input_text = input_text()

    # storing the gemini's response
    response = chatbot_actual(input_text)

    # response = example_usage() # to test the example_usage function

    # printing the response in chunks
    print(f"{Blue}Gemini: {Reset}", end="")
    for chunk in response:
        # time.sleep(0.1)
        print(chunk.text, end=" ")


if __name__ == "__main__":
    main()
