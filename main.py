import openai
import requests
import time

client = openai.OpenAI(
    api_key="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"
)


# a chatbot function
def chatbot_func(input: str, model="gpt-3.5-turbo"):
    time.sleep(5)
    # Define the API endpoint and headers
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {client.api_key}",
    }

    # Define the data payload
    data = {
        "model": model,
        "messages": [{"role": "user", "content": input}],
    }

    # Make the API request
    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        response_data = response.json()
        return response_data["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"


input = input("User: ")
answer = chatbot_func(input)
print(answer)
