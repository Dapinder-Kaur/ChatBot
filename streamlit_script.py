# importing necessary libraries
import streamlit as st
import random
import time
from PIL import Image
from google import genai
import main


# streamlit application function
def streamlit_app():
    image = Image.open("gemini.jpg")
    st.image(image, caption="Gemini", use_container_width=True)
    st.title("Gemini Chatbot")

    left_column, right_column = st.columns(2)

    left_column.write("How Can I Help You?")

    right_column.write("Gemini's Response")
    right_column.write("Gemini's response will appear here...")
    left_column.text_input("User: ", placeholder="Type your message here...")


def streamlit_app_design_2():

    st.title("Your personal Gemini")

    if "gemini_model" not in st.session_state:
        st.session_state["gemini_model"] = "gemini-2.0-flash"

    # having the history of the model
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # displaying chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Adding message to the chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

    functions = main.main()
    st.session_state.messages.append({"role": "user", "content": prompt})
    # st.session_state.messages.append({"role": "assistant", "content": response})

    # with st.chat_message("assistant"):
    #     stream = client.models.generate_content_stream(
    #         model=st.session_state["gemini_model"],
    #         contents=prompt,
    #     )
    #     response = st.write_stream(stream)

    # st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    streamlit_app_design_2()
