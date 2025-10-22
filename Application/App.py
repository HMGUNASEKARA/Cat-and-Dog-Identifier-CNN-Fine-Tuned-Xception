import streamlit as st
import tensorflow as tf
import numpy as np
import pickle 
import os
from PIL import Image

# Import the odel 
model_path = os.path.join("..","Model", "Final_model.keras")
model = tf.keras.models.load_model(model_path)


def main():
    with st.form("Form1"):
        st.title("Cat and Dog Classifier Application")
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        submit_button = st.form_submit_button(label="Classify Image")

    if submit_button:
        if uploaded_file is not None:
            # Load and preprocess the image
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image.', use_container_width=True)
            st.write("")
            st.write("Classifying...")

            # Preprocess the image
            image = image.resize((128, 128))
            image_array = np.array(image) / 255.0
            image_array = np.expand_dims(image_array, axis=0)

            

            # Make prediction
            prediction = model.predict(image_array)
            class_names = ['Cat', 'Dog']
            predicted_class = class_names[int(np.round(prediction[0][0]))]

            st.write(f'The uploaded image is classified as: **{predicted_class}**')
        else:
            st.write("Please upload an image file.")
if __name__ == "__main__":
    main()
