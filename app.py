import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64
import os
import fitz

logo_image_path = "TE_logo.png"
st.image(logo_image_path,width=200,caption ="Every Connection Counts")

def save_uploaded_file(uploaded_file,save_folder="uploads"):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    file_path = os.path.join(save_folder,uploaded_file.name)
    with open(file_path,"wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def read_pdf_content(file_path):
    content=""
    try:
        doc = fitz.open(file_path)
        for page_num in range(doc.page_count):
            page=doc[page_num]
            content+=page.get_text()
    except Exception as e:
        st.error(f"error while reading: {e}")
    return content

uploaded_file = st.file_uploader("Upload a file",type = ["csv","txt","xlsx","pdf"])

if uploaded_file is not None:
    st.write("file is uploaded")
    # st.write(uploaded_file)
    file_path = save_uploaded_file(uploaded_file)
    st.success(f"The file is here at: {file_path}")
    st.header("Read File Content")
    pdf_content = read_pdf_content(file_path)
    if pdf_content:
        st.text(pdf_content)

user_prompt = st.text_input("Enter Your Query: ")
st.button("Submit")
