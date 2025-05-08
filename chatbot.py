# importing the required libraries
from google import genai


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

API_KEY = "AIzaSyCRL3Ujbp6j-Gh1d1kO3PNWBLJqc5a1QGU"
# setting up the client with the API key
client = genai.Client(api_key="AIzaSyCRL3Ujbp6j-Gh1d1kO3PNWBLJqc5a1QGU")


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

    # time.sleep(0.1)
    return response


def chat_output(response):
    print(f"{Blue}Gemini: {Reset}", end="")
    for chunk in response:
        # time.sleep(0.1)
        print(chunk.text, end=" ")
