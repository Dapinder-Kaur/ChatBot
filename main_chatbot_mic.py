from google import genai
import os
from dotenv import load_dotenv
from main_chatbot import *
import sounddevice as sd
import speech_recognition as sr
from pydub import AudioSegment
from gtts import gTTS
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

load_dotenv()

client = genai.Client(
    api_key=os.environ.get("API_KEY"),
)


r = sr.Recognizer()


def actual_response():
    cond = True
    try:
        print("Get ready ..")
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            # print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while cond == True:
            user_input = input(
                "Press Enter if you are ready to Say something! or press 'w' if you wanna type: "
            )

            if user_input == "":
                print("Alright! Say your word !")
                with sr.Microphone() as source:
                    audio = r.listen(source=source, timeout=10)
                    print("Wait please...")
                try:
                    value = r.recognize_google(audio)
                    output = main_function(value)
                    response = text_to_speech(output)
                    response.save("assets/response.mp3")
                    chatbot_response = AudioSegment.from_mp3("assets/response.mp3")
                    play(chatbot_response)
                    # playsound(r"C:\Users\Riley\Documents\TACAM\ChatBot\response.mp3")
                    # print(output)yes

                except sr.UnknownValueError:
                    print("Oops! Didn't catch that")
                except sr.RequestError as e:
                    print(
                        "Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(
                            e
                        )
                    )

            elif user_input.lower() == "w":
                user = input("Enter here: ")
                output = main_function(user)
                response = text_to_speech(output)
                response.save("assets/response.mp3")
                chatbot_response = AudioSegment.from_mp3("assets/response.mp3")
                play(chatbot_response)

            else:
                cond = False
                print("Thank you, bye ..")
    except KeyboardInterrupt:
        pass


def main_function(audio):

    chat_history: list[types.Content] = []

    try:
        while True:
            input_text = audio
            print(f"{Yellow}User: {Reset}{input_text}")
            chat_history = history_function(chat_history, "user", input_text)
            response = response_system_prompt(chat_history)
            print(f"{Blue}ChatBot: {Reset}", end="")
            chunk_response = ""

            for chunk in response:
                print(chunk.text, end="")
                chunk_response += chunk.text

            chat_history = history_function(chat_history, "model", chunk_response)
            model_response = chunk_response
            return model_response

    except KeyboardInterrupt:
        print(f"\n{Red}Exiting .... {Reset}")
        sys.exit()


def text_to_speech(input_text: str):
    return gTTS(input_text)


if __name__ == "__main__":
    actual_response()
