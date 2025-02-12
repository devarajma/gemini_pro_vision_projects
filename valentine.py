import streamlit as st
import random
import time

# Function to generate love compatibility score
def calculate_love_score():
    return random.randint(50, 100)

# Function to determine love language based on score
def get_love_language(score):
    if score >= 90:
        return "💖 Physical Touch - You connect best through hugs, cuddles, and closeness!"
    elif score >= 80:
        return "💌 Words of Affirmation - Sweet words and compliments keep your love alive!"
    elif score >= 70:
        return "⏳ Quality Time - You cherish moments spent together more than anything!"
    elif score >= 60:
        return "🎁 Acts of Service - Love for you means doing little things that matter!"
    else:
        return "💝 Receiving Gifts - Thoughtful surprises make your heart melt!"

# Streamlit UI Design
st.markdown("<h1 style='text-align: center; color: red;'>💘 Valentine's Day Love Calculator 💘</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: pink;'>Upload your pictures and discover your love compatibility! 💑</h3>", unsafe_allow_html=True)

# Upload images
col1, col2 = st.columns(2)

with col1:
    boy_image = st.file_uploader("Upload Boy's Image", type=["jpg", "png", "jpeg"])

with col2:
    girl_image = st.file_uploader("Upload Girl's Image", type=["jpg", "png", "jpeg"])

# Calculate button
if st.button("💞 Calculate Love Score 💞"):
    if boy_image and girl_image:
        with st.spinner("Calculating love score... 💕"):
            time.sleep(2)  # Simulate processing delay
        
        love_score = calculate_love_score()
        love_language = get_love_language(love_score)

        # Display images side by side
        col1, col2 = st.columns(2)
        col1.image(boy_image, caption="💙 Boy", use_column_width=True)
        col2.image(girl_image, caption="💖 Girl", use_column_width=True)

        # Display Love Score
        st.markdown(f"<h2 style='text-align: center; color: red;'>❤️ Love Score: {love_score}% ❤️</h2>", unsafe_allow_html=True)

        # Love Meter Animation
        progress = st.progress(0)
        for i in range(love_score):
            time.sleep(0.02)
            progress.progress(i + 1)

        # Display Love Language
        st.markdown(f"<h3 style='text-align: center; color: purple;'>{love_language}</h3>", unsafe_allow_html=True)

        st.markdown("<h3 style='text-align: center; color: pink;'>💖 Happy Valentine's Day! 💖</h3>", unsafe_allow_html=True)
    else:
        st.warning("Please upload both images to calculate the love score!")

