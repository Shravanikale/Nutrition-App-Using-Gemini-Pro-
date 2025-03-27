from dotenv import load_dotenv  # Load environment variables
import streamlit as st  # Web UI framework
import os  # OS functions
import google.generativeai as genai  # Google AI API
from PIL import Image  # Image processing

# Load all environment variables from .env file
load_dotenv()

# Configure the API key securely
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="AI Nutritionist App")
st.title("Gemini Pro AI Health Management App")

st.header("AI Nutritionist App")

# User input for additional information (optional)
input_text = st.text_input("Input Prompt (Optional):", key="input")

# File uploader for image input
uploaded_file = st.file_uploader("Upload a food image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

def process_uploaded_image(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

def analyze_food_image(image_parts, input_text=""):
    """Analyzes food image and returns nutrition information"""
    
    # Update model to the latest version
    model = genai.GenerativeModel("gemini-1.5-flash")  # Changed from gemini-pro-vision

    # Default prompt
    input_prompt = """
    You are an expert in nutrition. Analyze the food items from the image and estimate the total calories.
    Provide details in the following format:

    1. Item Name - Calories
    2. Item Name - Calories
    ...
    """

    # Add user-provided input if available
    final_prompt = input_prompt if not input_text else input_prompt + "\nAdditional user input: " + input_text

    response = model.generate_content([final_prompt] + image_parts)
    return response.text

# Process button
if st.button("Analyze Food Image"):
    if uploaded_file:
        image_data = process_uploaded_image(uploaded_file)
        
        if image_data:
            with st.spinner("Analyzing food items... Please wait"):
                response = analyze_food_image(image_data, input_text)  # ✅ Now correctly passing both arguments
                
            st.subheader("Nutrition Analysis:")
            st.write(response)
        else:
            st.error("Error processing image. Please try again.")
    else:
        st.warning("Please upload an image first.")
