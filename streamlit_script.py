# # importing necessary libraries
# import streamlit as st
# import random
# import time
# from PIL import Image
# from google import genai
# from main import main
# from main import chatbot_actual_for_streamlit
# from main import client


# # streamlit application function
# def streamlit_app():
#     image = Image.open("gemini.jpg")
#     st.image(image, caption="Gemini", use_container_width=True)
#     st.title("Gemini Chatbot")

#     left_column, right_column = st.columns(2)

#     left_column.write("How Can I Help You?")

#     right_column.write("Gemini's Response")
#     right_column.write("Gemini's response will appear here...")
#     left_column.text_input("User: ", placeholder="Type your message here...")


# def streamlit_app_design_2():

#     st.title("Your personal Gemini")

#     if "gemini_model" not in st.session_state:
#         st.session_state["gemini_model"] = "gemini-2.0-flash"

#     # having the history of the model
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # displaying chat messages from history
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     # Accept user input
#     if prompt := st.chat_input(placeholder="What is up?"):
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)

#     with st.chat_message("assistant"):

#         stream = client.models.generate_content(
#             model="gemini-2.0-flash", contents=prompt
#         )

#     response = st.write_stream(stream)

#     st.session_state.messages.append({"role": "assistant", "content": response})


# if __name__ == "__main__":
#     streamlit_app_design_2()


# ======================================================


# # Set up the client with the API key
# client = client

# # Streamlit UI setup
# st.set_page_config(page_title="Your personal gemini", layout="centered")
# st.title("AI Chatbot")

# # Input box for user messages
# user_input = st.text_area("Enter your message:", key="input_text")


# # Function to get chatbot response
# def chatbot_response(input_text):
#     response = client.models.generate_content(
#         model="gemini-2.0-flash",
#         contents=input_text,
#     )
#     return response.text


# # Display response when button is clicked
# if st.button("Send"):
#     if user_input:
#         response = chatbot_response(user_input)
#         st.subheader("Chatbot Response:")
#         st.write(response)
#     else:
#         st.warning("Please enter a message before sending.")


# # ======================================================

# Trying something completely different
import os
import streamlit as st
from dotenv import load_dotenv
from functions import *
from main import API_KEY
from google import genai as gpt

load_dotenv()

st.set_page_config(
    page_titile="Baxter Chat",
    page_icon=":robot_face:",
    layout="wide",
)

API_KEY = os.getenv(API_KEY)

gpt.configure(api_key=API_KEY)
model = gpt.GenerativeModel("gemini-2.0-flash")

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("Baxter Chat")

for msg in st.session_state.chat_session.history:
    with st.chat_message(map_role(msg["role"])):
        st.markdown(msg["content"])


user_input = st.chat_input("Type your message here...")

if user_input:
    st.chat_message("user").markdown(user_input)

    gemini_response = fetch_gemini_response(user_input)

    with st.chat_message("assistant"):
        st.markdown(gemini_response)

st.session_state.chat_session.history.append({"role": "user", "content": user_input})
st.session_state.chat_session.history.append(
    {"role": "model", "content": gemini_response}
)
