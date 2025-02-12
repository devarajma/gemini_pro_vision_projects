

# import streamlit as st
# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Function to load Google Gemini Pro Vision API and get response
# def get_gemini_response(input_text, images):
#     model = genai.GenerativeModel('gemini-1.5-flash')
#     response = model.generate_content([input_text, images[0], images[1]])
#     return response.text

# # Function to process uploaded images
# def process_image(uploaded_file):
#     if uploaded_file is not None:
#         return {"mime_type": uploaded_file.type, "data": uploaded_file.getvalue()}
#     return None

# # Streamlit App Configuration
# st.set_page_config(page_title="Valentine's Love Matcher 💘", page_icon="❤️", layout="centered")

# # Valentine’s Day Theme
# st.markdown(
#     """
#     <style>
#         body {
#             background-color: #ffdde1;
#             background-image: linear-gradient(315deg, #ffdde1 0%, #ee9ca7 74%);
#         }
#         .title {
#             text-align: center;
#             font-size: 2.5em;
#             font-weight: bold;
#             color: #ff0055;
#         }
#         .subtitle {
#             text-align: center;
#             font-size: 1.5em;
#             color: #ff4081;
#         }
#         .result-box {
#             text-align: center;
#             padding: 15px;
#             background-color: pink;
#             border-radius: 10px;
#             box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.markdown("<h1 class='title'>💘 AI Love Matcher 💘</h1>", unsafe_allow_html=True)
# st.markdown("<h2 class='subtitle'>Upload two images & let AI predict your love match! ❤️</h2>", unsafe_allow_html=True)

# # Upload images for boy and girl
# col1, col2 = st.columns(2)

# with col1:
#     st.subheader("Upload Boy's Image")
#     boy_image_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], key="boy")

# with col2:
#     st.subheader("Upload Girl's Image")
#     girl_image_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], key="girl")

# # Display uploaded images
# if boy_image_file and girl_image_file:
#     col1, col2 = st.columns(2)
#     with col1:
#         st.image(boy_image_file, caption="Boy's Image", use_column_width=True)
#     with col2:
#         st.image(girl_image_file, caption="Girl's Image", use_column_width=True)

# submit = st.button("Find Your Love Match 💖")

# if submit:
#     if boy_image_file and girl_image_file:
#         boy_image_data = process_image(boy_image_file)
#         girl_image_data = process_image(girl_image_file)

#         # Input prompt for AI
        # input_prompt = """
        # Analyze the two images and provide only:
        # 1. A fun Love Compatibility Score (0-100%).
        # 2. Love Language of both.
        # Present it concisely and in a playful romantic way.
        # """

#         response = get_gemini_response(input_prompt, [boy_image_data, girl_image_data])

#         # Display the result in a fun styled box
#         st.markdown(f"<div class='result-box'><h2>💞 Love Match Result 💞</h2><p>{response}</p></div>", unsafe_allow_html=True)
#     else:
#         st.error("Please upload both images first! 💔")


import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(input_text, images):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, images[0], images[1]])
    return response.text

# Function to process uploaded images
def process_image(uploaded_file):
    if uploaded_file is not None:
        return {"mime_type": uploaded_file.type, "data": uploaded_file.getvalue()}
    return None

# Streamlit App Configuration
st.set_page_config(page_title="Valentine's Love Matcher 💘", page_icon="❤️", layout="centered")

# Valentine's Day Theme with CSS Styling
st.markdown(
    """
    <style>
        body {
            background-color: #ffdde1;
            background-image: linear-gradient(315deg, #ffdde1 0%, #ee9ca7 74%);
        }
        .title {
            text-align: center;
            font-size: 3em;
            font-weight: bold;
            color: #ff0055;
            text-shadow: 2px 2px 8px rgba(255, 0, 85, 0.5);
        }
        .subtitle {
            text-align: center;
            font-size: 1.6em;
            color: #ff4081;
            font-weight: bold;
            text-shadow: 1px 1px 6px rgba(255, 64, 129, 0.4);
        }
        .upload-box {
            background-color: rgba(255, 192, 203, 0.2);
            padding: 15px;
            border-radius: 10px;
            text-align: center;
        }
        .result-box {
            text-align: center;
            padding: 20px;
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(255, 0, 85, 0.3);
            font-size: 1.3em;
            font-weight: bold;
            color: white;
            animation: glow 1.5s infinite alternate;
        }
        @keyframes glow {
            from {box-shadow: 0px 4px 15px rgba(255, 0, 85, 0.6);}
            to {box-shadow: 0px 4px 25px rgba(255, 0, 85, 0.9);}
        }
        .button {
            display: flex;
            justify-content: center;
        }
        .love-btn {
            background-color: #ff4081;
            color: white;
            font-size: 1.2em;
            font-weight: bold;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            box-shadow: 2px 2px 8px rgba(255, 64, 129, 0.5);
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .love-btn:hover {
            background-color: #e91e63;
            transform: scale(1.05);
            box-shadow: 2px 2px 12px rgba(255, 64, 129, 0.7);
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='title'>💘 AI Love Matcher 💘</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitle'>Upload two images & let AI reveal your love match! ❤️</h2>", unsafe_allow_html=True)

# Upload images for boy and girl
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='upload-box'><h3>💙 Upload Partner 1</h3></div>", unsafe_allow_html=True)
    boy_image_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], key="boy")

with col2:
    st.markdown("<div class='upload-box'><h3>💖 Upload Partner 2</h3></div>", unsafe_allow_html=True)
    girl_image_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], key="girl")

# Display uploaded images
if boy_image_file and girl_image_file:
    col1, col2 = st.columns(2)
    with col1:
        st.image(boy_image_file, caption="💙 Partner 1", use_column_width=True)
    with col2:
        st.image(girl_image_file, caption="💖 Partner 2", use_column_width=True)

# Love Button
# st.markdown("<div class='button'><button class='love-btn'>💖 Find Your Love Match 💖</button></div>", unsafe_allow_html=True)
submit = st.button("Find Your Love Match 💖")

if submit:
    if boy_image_file and girl_image_file:
        boy_image_data = process_image(boy_image_file)
        girl_image_data = process_image(girl_image_file)

        # Input prompt for AI
        input_prompt = """
        Analyze the two images and provide only:
        1. A fun Love Compatibility Score (0-100%).
        2. Love Language of both.
        Present it concisely and in a playful romantic way.
        """

        response = get_gemini_response(input_prompt, [boy_image_data, girl_image_data])

        # Display the result in a glowing styled box
        st.markdown(f"<div class='result-box'><h2>💞 Love Match Result 💞</h2><p>{response}</p></div>", unsafe_allow_html=True)
    else:
        st.error("Please upload both images first! 💔")
