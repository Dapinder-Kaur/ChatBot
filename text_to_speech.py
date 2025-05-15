from gtts import gTTS
import os
from speech_to_text import *


def text_to_speech(input_text: str):
    return gTTS(input_text)


value_output = main_function()
text = text_to_speech(value_output)

text.save("response.mp3")
os.system("response.mp3")
