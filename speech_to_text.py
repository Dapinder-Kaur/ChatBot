from google import genai
import os
from dotenv import load_dotenv
from main import *
import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import scipy.io.wavfile as wav
from pydub import AudioSegment

load_dotenv()

client = genai.Client(
    api_key=os.environ.get("API_KEY"),
)


recognizer = sr.Recognizer()
fs = 44100
seconds = 1


def speechtotext():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source=source)
        text = r.recognize_google(audio)
        return text


def recording_function():
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()

    filename_input = "output.WAV"
    write(filename_input, fs, myrecording)
    return filename_input


# myfile = client.files.upload(
#     file=r"C:\Users\Riley\Documents\Audio_files\hello-46355.mp3"
# )
def gemini_response_function(input_f):
    myfile = client.files.upload(file=input_f)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            "Only transcribe this audio clip, do not write anything extra, do not say anything from your side",
            myfile,
        ],
    )

    return response.text


def actual_response_function(audio_in):
    output_path = "output_fixed.wav"

    audio = AudioSegment.from_file(r"C:\Users\Riley\Documents\TACAM\ChatBot\output.wav")
    audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
    audio.export(output_path, format="wav")
    try:
        with sr.AudioFile(output_path) as source:
            audio_data = recognizer.record(source)

            text = recognizer.recognize_google(audio_data)
            if text == "":
                text = "hi"

            return text

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


model_response = ""


def main_function():
    global model_response
    chat_history: list[types.Content] = []
    len_files = 1
    n = 1
    try:
        while True:
            input_text = speechtotext()
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

            n += 1
    except KeyboardInterrupt:
        print(f"\n{Red}Exiting .... {Reset}")
        sys.exit()


def actual_response_function_for_gradio(audio_path):
    output_path = "output_fixed.wav"

    audio = AudioSegment.from_file(audio_path)
    audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
    audio.export(output_path, format="wav")
    try:
        with sr.AudioFile(output_path) as source:
            audio_data = recognizer.record(source)

            text = recognizer.recognize_google(audio_data)

            return text

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main_function()
