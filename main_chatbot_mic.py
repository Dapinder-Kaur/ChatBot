from google import genai
import os

import sys
import sounddevice as sd
import speech_recognition as sr
from pydub import AudioSegment
from gtts import gTTS
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
import chatbot as cb


client = cb.client


r = sr.Recognizer()


def actual_response():
    cond = True

    try:
        print("Get ready ..")
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)

        while cond == True:
            user_input = input(
                "Press Enter if you are ready to Say something! or press 'w' if you wanna type: "
            )

            if user_input == "":
                print("Alright! Say your word !")

                try:
                    with sr.Microphone() as source:
                        audio = r.listen(source=source, timeout=10)
                        print("Wait please...")

                    value = r.recognize_google(audio)

                    if value == None:
                        print("Try again please, could not hear")
                        continue

                    output = main_function(value)
                    response = text_to_speech(output)
                    response.save("assets/response.mp3")
                    chatbot_response = AudioSegment.from_mp3("assets/response.mp3")
                    play(chatbot_response)

                except sr.UnknownValueError:
                    print("Oops! Didn't catch that")

                except sr.WaitTimeoutError:
                    print("Try again")

                except sr.RequestError as e:
                    print("Couldn't request results from Google; {0}".format(e))

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

    chat_history: list[cb.types.Content] = []

    try:
        while True:
            input_text = audio
            print(f"{cb.Yellow}User: {cb.Reset}{input_text}")
            chat_history = cb.history_function(chat_history, "user", input_text)
            response = cb.response_system_prompt(chat_history)
            print(f"{cb.Blue}ChatBot: {cb.Reset}", end="")
            chunk_response = ""

            for chunk in response:
                print(chunk.text, end="")
                chunk_response += chunk.text

            chat_history = cb.history_function(chat_history, "model", chunk_response)
            model_response = chunk_response
            return model_response

    except KeyboardInterrupt:
        print(f"\n{cb.Red}Exiting .... {cb.Reset}")
        sys.exit()


def text_to_speech(input_text: str):
    return gTTS(input_text)


if __name__ == "__main__":
    actual_response()
