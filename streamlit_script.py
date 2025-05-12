import streamlit as st

from chatbot import (
    chatbot_response,
    output_function,
    chat_output,
    chatbot_stream_response,
    input_text,
)

st.title("Your personal Chatbot")

left_column, right_column = st.columns(2)

user_input = input_text()
left_column.text_input("How Can I help: ", user_input, key="input_text")


with right_column:
    output = chatbot_response(user_input)
    output_final = output_function(output)
    st.write("Gemini")
    st.write(output_final)


output_print = chatbot_stream_response(user_input)


# st.session_state.input_text


chat_output(output_print)
