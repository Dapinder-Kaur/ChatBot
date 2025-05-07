# importing necessary libraries
import streamlit as st
import random
import time
from PIL import Image
from google import genai
from main import main
from main import chatbot_actual_for_streamlit
from main import client


# client = client
# from main import input_text


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

#         response = chatbot_actual_for_streamlit(prompt)

#     st.session_state.messages.append({"role": "assistant", "content": response})


# if __name__ == "__main__":
#     streamlit_app_design_2()


# Set up the client with the API key
client = client

# Streamlit UI setup
st.set_page_config(page_title="Chatbot Interface", layout="centered")
st.title("AI Chatbot")

# Input box for user messages
user_input = st.text_area("Enter your message:", key="input_text")


# Function to get chatbot response
def chatbot_response(input_text):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=input_text,
    )
    return response.text


# Display response when button is clicked
if st.button("Send"):
    if user_input:
        response = chatbot_response(user_input)
        st.subheader("Chatbot Response:")
        st.write(response)
    else:
        st.warning("Please enter a message before sending.")

# Run the script using: `streamlit run streamlit_script.py`
