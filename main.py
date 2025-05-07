from google import genai

client = genai.Client(api_key="AIzaSyCRL3Ujbp6j-Gh1d1kO3PNWBLJqc5a1QGU")


def example_usage():
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Explain how AI works in a few words",
    )
    return response.text


def chatbot_actual(input_text):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=input_text,
    )
    return response.text


# input_text = input("User: ")
# response = chatbot_actual(input_text)
response = example_usage()

print(response)
