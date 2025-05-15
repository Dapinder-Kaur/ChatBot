from google import genai
import os
from dotenv import load_dotenv
from main import *
import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import scipy.io.wavfile as wav
from pydub import AudioSegment
from pydub.playback import play


def speechtotext():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        return text


# val = speechtotext()
# print(val)

song = AudioSegment.from_mp3("response.mp3")
play(song)
