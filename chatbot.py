# importing the required libraries
from google import genai


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
