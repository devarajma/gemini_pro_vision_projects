from dotenv import load_dotenv

load_dotenv()  # load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0]])
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

# Initialize our Streamlit app
st.set_page_config(page_title="Know Your Food App", page_icon="🍎", layout="centered", initial_sidebar_state="expanded")

# Sidebar content
with st.sidebar:
    st.header("Navigation")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    st.markdown("___")
    dark_mode = st.checkbox("Dark Mode")
    st.session_state.dark_mode = dark_mode

# Apply custom CSS for additional styling
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

if st.session_state.dark_mode:
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');

        .main {
            background-color: #333333;
            color: #ffffff;
            font-family: 'Roboto', sans-serif;
        }
        .stButton>button {
            background-color: #0d6efd;
            color: white;
            font-size: 18px;
            font-family: 'Playfair Display', serif;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #b2d0ed;
            color: white;
            border-color:
        }
        .stTextInput>div>input {
            border-radius: 8px;
            font-size: 16px;
            font-family: 'Roboto', sans-serif;
            padding: 10px;
            border: 1px solid #cccccc;
        }
        .stHeader {
            font-family: 'Playfair Display', serif;
            font-size: 36px;
            font-weight: 700;
            color: #0d6efd;
            margin-bottom: 20px;
        }
        .stSubheader {
            font-family: 'Playfair Display', serif;
            font-size: 24px;
            font-weight: 400;
            color: #ffffff;
            margin-bottom: 20px;
        }
        .stMarkdown {
            font-family: 'Roboto', sans-serif;
            font-size: 18px;
            color: #ffffff;
        }
        .sidebar .sidebar-content {
            background-color: #444444;
            padding: 20px;
        }
        .sidebar .sidebar-content h4 {
            color: #ffffff;
        }
        .sidebar .sidebar-content small {
            color: #cccccc;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');

        .main {
            background-color: #f8f9fa;
            color: #333333;
            font-family: 'Roboto', sans-serif;
        }
        .stButton>button {
            background-color: #0d6efd;
            color: white;
            font-size: 18px;
            font-family: 'Playfair Display', serif;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #0a58ca;
            color: white;
        }
        .stTextInput>div>input {
            border-radius: 8px;
            font-size: 16px;
            font-family: 'Roboto', sans-serif;
            padding: 10px;
            border: 1px solid #cccccc;
        }
        .stHeader {
            font-family: 'Playfair Display', serif;
            font-size: 36px;
            font-weight: 700;
            color: #0d6efd;
            margin-bottom: 20px;
        }
        .stSubheader {
            font-family: 'Playfair Display', serif;
            font-size: 24px;
            font-weight: 400;
            color: #333333;
            margin-bottom: 20px;
        }
        .stMarkdown {
            font-family: 'Roboto', sans-serif;
            font-size: 18px;
            color: #333333;
        }
        .sidebar .sidebar-content {
            background-color: #e9ecef;
            padding: 20px;
        }
        .sidebar .sidebar-content h4 {
            color: #333333;
        }
        .sidebar .sidebar-content small {
            color: #666666;
        }
        </style>
    """, unsafe_allow_html=True)

# Main content
st.markdown("<h1 class='stHeader'>Know Your Food App</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='stSubheader'>Analyze your food and get detailed nutritional information</h2>", unsafe_allow_html=True)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me the total calories")

input_prompt = """
You are an expert nutritionist where you need to see the food items from the image
and calculate the total calories. Also provide the details of every food item with calories intake
in the following format:

1. Item 1 - no of calories
2. Item 2 - no of calories
----
----
Finally, mention whether the food is healthy or not and also mention the percentage split of carbohydrates, fats, fibers, sugar, and other important things required in our diet.
"""

if submit:
    if uploaded_file is not None:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt, image_data)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.error("Please upload an image first.")
