from google import genai

import sys
import chatbot_functions as cb
import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import scipy.io.wavfile as wav
from pydub import AudioSegment


client = cb.client
recognizer = sr.Recognizer()
fs = 44100
seconds = 1


def speechtotext():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source=source)
        text = r.recognize_google(audio)
        return text

    except sr.UnknownValueError:
        print("Could not understand.")

    except sr.WaitTimeoutError:
        print("Try again!!")


def recording_function():
    my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    filename_input = "output.WAV"
    write(filename_input, fs, my_recording)
    return filename_input


# function for using gemini to transcribe the text
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


# when reading an input file and audio data is not in .wav format
def actual_response_function():
    output_path = "output_fixed.wav"

    # the file path can be replaced with the actual path
    audio = AudioSegment.from_file(r"C:\Users\Riley\Documents\TACAM\ChatBot\output.wav")

    audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
    audio.export(output_path, format="wav")

    try:
        with sr.AudioFile(output_path) as source:
            audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        return text

    except sr.UnknownValueError:
        print("Could not understand audio")
        text = " "
        return text

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    except Exception as e:
        print(f"An error occurred: {e}")


model_response = ""


def speech_to_text():
    global model_response
    chat_history: list[cb.types.Content] = []

    try:
        while True:
            input_text = speechtotext()

            if input_text == None:
                sys.exit("Try to speak again.")

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


if __name__ == "__main__":
    speech_to_text()
