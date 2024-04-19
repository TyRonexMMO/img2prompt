import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key="AIzaSyBZQmot8_8bDxuGiffJ06woJCzH140Erc4")

def get_response(inputt, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if inputt != "":
        response = model.generate_content((inputt, image))
    else:
        response = model.generate_content(image)
    return response.text

st.header("My project")
inputt = st.text_input("input prompt", key='input')
uploaded_file = st.file_uploader("Choose you file", type=["jpg", "jpeg", "png"])
image =''
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='uploaded_image', use_column_width= True)

submit = st.button('Ask')
if submit:
    response = get_response(inputt, image)
    st.write(response)