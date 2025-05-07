# importing necessary libraries
import streamlit as st
from PIL import Image


# streamlit application function
def streamlit_app():
    image = Image.open("gemini.jpg")
    st.image(image, caption="Gemini", use_container_width=True)
    st.title("Gemini Chatbot")


if __name__ == "__main__":
    streamlit_app()
