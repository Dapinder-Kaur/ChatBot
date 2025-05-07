import requests
import google.generativeai as genai
import time


GOOGLE_API_KEY = "AIzaSyD_nRcAau-qH_I_1tRQ5RTIaaGR67oBwyY"
genai.configure(api_key=GOOGLE_API_KEY)


# a chatbot function
def chatbot_func(input: str, model=genai.GenerativeModel("gemini-1.5-pro-002")):

    # Make the API request
    chat = model.start_chat(history=[])

    response = chat.send_message(input, stream=True)
    return response.text


input = input("User: ")
answer = chatbot_func(input)
print(answer)
