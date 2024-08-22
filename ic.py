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

# Use an external URL for the background image
bg_image_url = "https://in.images.search.yahoo.com/images/view;_ylt=AwrKBBJMXcdmAOIBCXq9HAx.;_ylu=c2VjA3NyBHNsawNpbWcEb2lkAzE5NmViYTg5MDJiZGI5YmFmMDNmMWE0YjA5MmVhOWM2BGdwb3MDMQRpdANiaW5n?back=https%3A%2F%2Fin.images.search.yahoo.com%2Fsearch%2Fimages%3Fp%3Dnature%2Bimages%26type%3DE210IN885G0%26fr%3Dmcafee%26fr2%3Dpiv-web%26tab%3Dorganic%26ri%3D1&w=1920&h=1440&imgurl=wallpaperaccess.com%2Ffull%2F1688623.jpg&rurl=https%3A%2F%2Fwallpaperaccess.com%2Fnature-scenery&size=685.8KB&p=nature+images&oid=196eba8902bdb9baf03f1a4b092ea9c6&fr2=piv-web&fr=mcafee&tt=Nature+Scenery+Wallpapers+-+Top+Free+Nature+Scenery+Backgrounds+...&b=0&ni=21&no=1&ts=&tab=organic&sigr=mQhhBN7XtcD7&sigb=o3uo2PapXcwO&sigi=DH_lSpCBP_Pc&sigt=dhN8v_YC3Oz3&.crumb=2b0tlBiWEP8&fr=mcafee&fr2=piv-web&type=E210IN885G0"  # Replace with your image URL

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("{bg_image_url}");
background-size: cover;
}}
[data-testid="stHeader"] {{
background: rgba(0, 0, 0, 0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
