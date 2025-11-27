# ChatBot

A small, modular chatbot project demonstrating:
- Command-line chat interface
- Streaming output (word-by-word printing)
- Gradio UI integration
- Microphone input and audio output (speech-to-text and text-to-speech)

This repository is organized so you can iterate quickly between CLI, UI, and audio-powered interactions.

## Features
- Basic conversational loop: see [chatbot.py](chatbot.py)
- Streaming text output for an animated response: see [main_chatbot.py](main_chatbot.py)
- Gradio web UI: see [main_gradio.py](main_gradio.py)
- Microphone-enabled clients: [main_chatbot_mic.py](main_chatbot_mic.py), [main_gradio_mic.py](main_gradio_mic.py)
- Audio helpers: [speech_to_text.py](speech_to_text.py), [text_to_speech.py](text_to_speech.py)

## Requirements
- Python 3.8+
- Create a virtual environment and install your dependencies:
```sh
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS / Linux
```

## Quickstart

1. CLI chat:
```sh
python main_chatbot.py
```
2. Animated/streamed CLI:
```sh
python main_chatbot.py 
```
3. Gradio UI:
```sh
python main_gradio.py
```
4. Microphone-enabled chat (local mic → STT → model → TTS):
```sh
python main_chatbot_mic.py
# or
python main_gradio_mic.py
```

See the corresponding files for flags and customization:
- [main_chatbot.py](main_chatbot.py)
- [main_gradio.py](main_gradio.py)
- [main_chatbot_mic.py](main_chatbot_mic.py)
- [main_gradio_mic.py](main_gradio_mic.py)

## Testing
Run the test scripts in the `tests/` folder:
```sh
python -m pytest tests/
```
Tests present: [tests/test.py](tests/test.py), [tests/test_2.py](tests/test_2.py), [tests/test_gradio_mic.py](tests/test_gradio_mic.py), [tests/test_streamlit.py](tests/test_streamlit.py)

### Happy Coding !!
