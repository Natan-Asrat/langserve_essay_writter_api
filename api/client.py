import requests
import streamlit as st

def get_essay_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke", json={
        'input':{'topic': input_text}
    })
    print(response.json())
    return response.json()['output']['content']


st.title('Langchain Essay Writter with Groq API')
input_text = st.text_input("Write an essay on")

if input_text:
    st.write(get_essay_response(input_text))