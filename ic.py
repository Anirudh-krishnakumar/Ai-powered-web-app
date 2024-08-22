import requests
import streamlit as st
import os

# Title of the app
st.title("Anik_Ai")

# API URL and headers
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

# Function to query the API
def query(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

# Ensure the directory exists
upload_dir = 'uploaded_files'
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

# File uploader
a = st.file_uploader("Upload an image", type='jpg')

if a is not None:
    # Define the file path
    file_path = os.path.join(upload_dir, a.name)
    
    # Save the uploaded file
    with open(file_path, "wb") as f:
        f.write(a.getbuffer())

    # Call the query function with the file path
    try:
        output = query(file_path)[0]['generated_text']

        st.text(output)
    except FileNotFoundError:
        st.error(f"File not found: {file_path}")
    except Exception as e:
        st.error(f"An error occurred while querying: {e}")
else:
    st.info("Please upload an image file.")


import base64

def get_img_as_base64(file):
    with open(file,"rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
img = get_img_as_base64("a.jpg")

page_bg_img = f"""

<style>
[data-testid="stAppViewContainer"] > .main {{
background-image :url("data:image/png;base64,{img}");
background-size : cover;
}}
[data-testid="stHeader"]{{
background:rgba(0,0,0,0);
}}
</style>

"""
st.markdown(page_bg_img, unsafe_allow_html=True)