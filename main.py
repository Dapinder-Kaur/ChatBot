from google import genai
import time

client = genai.Client(api_key="AIzaSyCRL3Ujbp6j-Gh1d1kO3PNWBLJqc5a1QGU")


def example_usage():
    response = client.models.generate_content_stream(
        model="gemini-2.0-flash", contents="Hi, How are you?"
    )
    return response


def chatbot_actual(input_text):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=input_text,
    )
    return response.text


input_text = input("User: ")
response: str = chatbot_actual(input_text)
# response = example_usage()


def print_response(response):
    for chunk in response.split(" "):
        time.sleep(0.3)
        print(chunk, end=" ", flush=True)


print_response(response)
