# importing necessary libraries
import streamlit as st
from PIL import Image
import main


# streamlit application function
def streamlit_app():
    image = Image.open("gemini.jpg")
    st.image(image, caption="Gemini", use_container_width=True)
    st.title("Gemini Chatbot")

    left_column, right_column = st.columns(2)

    left_column.write("How Can I Help You?")

    right_column.write("Gemini's Response")
    right_column.write(placeholder="Gemini's response will appear here...")
    left_column.text_input("User: ", placeholder="Type your message here...")


if __name__ == "__main__":
    streamlit_app()
