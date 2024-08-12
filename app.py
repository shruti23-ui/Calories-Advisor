import streamlit as st
import google.generativeai as genai 
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, image, portion_size):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([input_prompt, image[0], portion_size])
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

# Initialise streamlit-frontend-setup
st.set_page_config(page_title="Calories Advisor App")
st.header("Calories Advisor App")

# File uploader for image
uploaded_file = st.file_uploader("Choose an image....", type=["jpg", "jpeg", "png"])

# Text input for portion size
portion_size = st.text_input("Enter the portion size (e.g., 200 grams):")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Analyze calories")

input_prompt = """
You are an expert in nutrition where you need to see the food items from the image
and calculate the total calories, also provide the details of every food item with calorie intake in the format below:
Discuss possible ingredients, suggest general calorie content if possible, and provide advice on the overall healthiness of the food. 
If exact calculations are not feasible, share general tips for estimating calorie content and nutritional balance.
1. Item 1 - no. of calories
2. Item 2 - no. of calories
----
----
also keep following points in mind
1. Discuss possible ingredients and provide general calorie content estimates if feasible and if it seems impossible to tell just by the image, don't give the response like that. Response should be possible and optimistic only.
2. Offer advice on the overall healthiness of the food.
3. If exact calculations are not possible, suggest general tips for estimating calorie content and achieving a balanced diet.
4. List possible items and their calorie estimates if recognizable.
5. Don't mention what you cannot tell.

Provide insights on carbohydrates, vitamins, fats, fibers, sugars, and other key nutrients.

Finally, you can also mention whether the food is healthy or not and also mention the
percentage split of the ratio of carbohydrates, vitamins, fats, fibers, sugars, and other important things in our diet.
"""

if submit:
    if uploaded_file is not None and portion_size:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt, image_data, portion_size)
        st.header("The Response is")
        st.write(response)
    else:
        st.write("Please upload an image and provide portion size.")
