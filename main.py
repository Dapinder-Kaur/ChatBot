import requests
import google.generativeai as genai
import time

GOOGLE_API_KEY = "AIzaSyBvUiuvXnWsvV3qpBKBPHas9jrBN_YB1jk"
genai.configure(api_key=GOOGLE_API_KEY)


# a chatbot function
def chatbot_func(input: str, model=genai.GenerativeModel("gemini")):

    # Make the API request
    chat = model.start_chat(history=[])

    response = chat.send_message(input, stream=False)
    return response.text


input = input("User: ")
answer = chatbot_func(input)
print(answer)
