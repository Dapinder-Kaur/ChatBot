from gtts import gTTS
import speech_to_text
from pydub.playback import play
from pydub import AudioSegment


def text_to_speech(input_text: str):
    return gTTS(input_text)


value_output = speech_to_text.speech_to_text()
text = text_to_speech(value_output)

text.save("assets/response.mp3")
chatbot_response = AudioSegment.from_mp3("assets/response.mp3")
play(chatbot_response)
