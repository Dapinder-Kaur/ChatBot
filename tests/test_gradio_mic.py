import gradio as gr
import speech_recognition as sr


def audio_to_text(audio_file_path):
    """Converts audio from a file path to text."""
    r = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"


def process_audio(audio):
    """Processes the audio input, transcribes it, and returns the text."""
    if audio is None:
        return "No audio recorded"

    text = audio_to_text(audio)
    return text


iface = gr.Interface(
    fn=process_audio,
    inputs=gr.Audio(sources=["microphone"], type="filepath"),
    outputs="text",
    title="Audio to Text Conversion",
    description="Record audio and convert it to text using speech recognition.",
)

if __name__ == "__main__":
    iface.launch()
