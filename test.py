import requests
import speech_recognition as sr
import sounddevice as sd
import scipy.io.wavfile as wav
from scipy.io.wavfile import write

recognizer = sr.Recognizer()
fs = 44100
seconds = 1

print(requests.get("http://www.google.com").status_code)


# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
# sd.wait()

# filename_input = "output.WAV"
# write(filename_input, fs, myrecording)
# filename_input

from pydub import AudioSegment

# test_input = r"C:\Users\Riley\Documents\Audio_files\hello-46355.mp3"


# def convert_audio(input_file, output_file):
#     audio = AudioSegment.from_file(input_file)  # Auto-detect format
#     audio = (
#         audio.set_frame_rate(1600).set_channels(2).set_sample_width(2)
#     )  # Ensure compatibility
#     audio.export(output_file, format="wav")  # Convert to WAV
#     return output_file


# # Example usage
# converted_file = convert_audio(test_input, "test_output.wav")
# print(f"Converted file saved as: {converted_file}")


# try:
#     with sr.AudioFile(
#         filename_or_fileobject=r"C:\Users\Riley\Documents\TACAM\ChatBot\output.wav"
#     ) as source:
#         audio_data = recognizer.record(source=source)

#         text = recognizer.recognize_tensorflow(audio_data=audio_data)
#         print(text)


# except sr.UnknownValueError:
#     print("Could not understand audio")
#     text = "hi"

# except sr.RequestError as e:
#     print(f"Could not request results from Google Speech Recognition service; {e}")
#     text = "hi"

# except Exception as e:
#     print(f"An error occurred: {e}")
#     text = "hi"


import speech_recognition as sr

recognizer = sr.Recognizer()
print([method for method in dir(recognizer) if method.startswith("recognize")])


import numpy as np

# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
# sd.wait()

# # Convert float32 to int16 (required for PCM WAV)
# myrecording_int16 = np.int16(myrecording * 32767)

# filename_input = "output.wav"
# write(filename_input, fs, myrecording_int16)

# audio_file = (
#     r"C:\Users\Riley\Documents\Audio_files\ca39d23e5ddd28dbb7992064b3ee-orig.wav"
# )
# myrecording_int16 = np.int16(audio_file * 32767)

# filename_input = "output.wav"
# write(filename_input, fs, myrecording_int16)

# with sr.AudioFile(filename_or_fileobject=filename_input) as source:
#     audio_data = recognizer.record(source=source)

#     text = recognizer.recognize_google(audio_data=audio_data)
#     print(text)
import speech_recognition as sr
from pydub import AudioSegment

# File paths
input_path = r"C:\Users\Riley\Downloads\harvard.wav"
output_path = "output_fixed.wav"

# Convert the audio file to 16kHz mono WAV
audio = AudioSegment.from_file(input_path)
audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
audio.export(output_path, format="wav")

# Recognize speech from the converted file
recognizer = sr.Recognizer()

with sr.AudioFile(output_path) as source:
    audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
        print("Transcription:", text)
    except sr.UnknownValueError:
        print("Speech was unintelligible")
    except sr.RequestError as e:
        print(f"API request error: {e}")
