from gtts import gTTS
import os
from speech_to_text import *
from pydub.playback import play


def text_to_speech(input_text: str):
    return gTTS(input_text)


value_output = main_function()
text = text_to_speech(value_output)

text.save("assets/response.mp3")
chatbot_response = AudioSegment.from_mp3("assets/response.mp3")
play(chatbot_response)
