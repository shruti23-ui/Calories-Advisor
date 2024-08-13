import streamlit as st
import google.generativeai as genai 
import os
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the model as gemini-1.5-pro
model = genai.GenerativeModel('gemini-1.5-pro')

def get_gemini_response(input_prompt, image, portion_size=None):
    # Create input list based on whether portion size is provided
    inputs = [input_prompt, image[0]]
    if portion_size:
        inputs.append(portion_size)
    
    response = model.generate_content(inputs)
    return response.text

def input_image_setup(uploaded_file):
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

# Initialize Streamlit frontend setup
st.set_page_config(page_title="Calories Advisor App")
st.header("Calories Advisor App")

# File uploader for image
uploaded_file = st.file_uploader("Choose an image....", type=["jpg", "jpeg", "png"])

# Text input for portion size (optional)
portion_size = st.text_input("Enter the portion size (e.g., 200 grams):")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Analyze calories")

input_prompt = """
You are an expert in nutrition. Analyze the food items in the image and estimate the total calories. Provide details of every recognizable food item with estimated calorie intake in the format below:

1. Item 1 - no. of calories
2. Item 2 - no. of calories
----
----
Please consider the following:

1. Offer confident estimations based on visual cues and general knowledge.
2. Avoid mentioning any limitations or uncertainties. Focus on providing helpful, optimistic insights.
3. Suggest advice on the overall healthiness of the food.
4. List possible ingredients, their calorie estimates, and advice on achieving a balanced diet.
5. Provide insights on carbohydrates, vitamins, fats, fibers, sugars, and other key nutrients.
6. Conclude with a statement on whether the food is generally healthy and suggest a percentage split of nutrients (carbohydrates, vitamins, fats, fibers, sugars) for a balanced diet.
"""

if submit:
    if uploaded_file is not None:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt, image_data, portion_size)
        st.header("The Response is")
        st.write(response)
    else:
        st.write("Please upload an image.")
