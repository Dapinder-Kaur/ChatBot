import streamlit as st
from main import input_text
from chatbot import (
    chatbot_response,
    output_function,
    chat_output,
    chatbot_stream_response,
)

st.title("Your personal Chatbot")

left_column, right_column = st.columns(2)

input = input_text()
left_column.text_input("How Can I help: ", input, key="input_text")
st.button("Submit", key="submit_button")

output_print = chatbot_stream_response(input)


# st.session_state.input_text
with right_column:
    output = chatbot_response(input)
    output_final = output_function(output)
    st.write("Gemini")
    st.write(output_final)

chat_output(output_print)
