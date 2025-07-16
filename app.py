import streamlit as st
import tensorflow as tf
import numpy as np
import os

MODEL_PATH = "sentiment_lstm_model.h5"

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

st.title("LSTM Model Demo")
user_input = st.text_input("Input comma-separated values:")

if user_input:
    try:
        # Convert input string to numpy array (assuming your model expects numeric input)
        input_data = np.array([float(x.strip()) for x in user_input.split(",")])
        input_data = np.expand_dims(input_data, axis=0)  # add batch dimension

        model = load_model()
        prediction = model.predict(input_data)
        st.write(f"Model prediction: {prediction}")
    except Exception as e:
        st.error(f"Error: {e}")