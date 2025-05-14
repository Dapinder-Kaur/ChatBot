from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.environ.get("API_KEY"),
)

myfile = client.files.upload(
    file=r"C:\Users\Riley\Documents\Audio_files\hello-46355.mp3"
)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=["Only transcript this audio clip", myfile]
)

print(response.text)
