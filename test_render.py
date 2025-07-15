import os
import requests
import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np

# Hugging Face direct download URL
MODEL_URL = "https://huggingface.co/cckmwong/sentiment/resolve/main/sentiment_lstm_model.h5"
MODEL_PATH = "sentiment_lstm_model.h5"

@st.cache_resource
def get_model():
    if not os.path.exists(MODEL_PATH):
        with st.spinner("Downloading model..."):
            r = requests.get(HF_MODEL_URL)
            with open(MODEL_PATH, "wb") as f:
                f.write(r.content)
    model = load_model(MODEL_PATH)
    return model

model = get_model()

# UI Example
st.title("LSTM Model Demo")
user_input = st.text_input("Input comma-separated values:")