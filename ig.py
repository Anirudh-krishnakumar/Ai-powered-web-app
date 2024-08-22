
import streamlit as st

import requests
st.title("Anik_Ai")
a=st.text_input("enter text")
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization":  "Bearer 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"}


def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": a,
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))
if (st.button("create")):
	
	st.image(image)
