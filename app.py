import streamlit as st
from PIL import Image
from models.model_loader import load_model
from utils.image_processor import generate_caption

st.set_page_config(page_title="VisionaryLens - Image Caption Generator")
st.title("VisionaryLens - Image Caption Generator")

st.write("Streamlit version:", st.__version__)

st.write("Loading model...")
try:
    model, processor = load_model()
    st.write("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)


    if st.button("Generate Caption"):
        try:
            caption = generate_caption(image, model, processor)
            st.success(f"Generated Caption: {caption}")
        except Exception as e:
            st.error(f"Error generating caption: {e}")


