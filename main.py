import openai
import requests
from openai import OpenAI
import time

client = OpenAI(
    api_key="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"
)


# a chatbot function
def chatbot_func(input: str, model="gpt-3.5-turbo"):

    # Make the API request
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": input}],
    )

    # Check if the request was successful
    if response.status_code == 200:
        response_data = response.json()
        return response_data["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"


input = input("User: ")
answer = chatbot_func(input)
print(answer)
