import streamlit as st
import random
import time
import pandas as pd
from PIL import Image
import os

# Set page configuration
st.set_page_config(page_title="Love Calculator ❤️", page_icon="💘", layout="centered")

# File for storing leaderboard
LEADERBOARD_FILE = "leaderboard.csv"

# Load existing leaderboard data
if os.path.exists(LEADERBOARD_FILE):
    leaderboard = pd.read_csv(LEADERBOARD_FILE)
else:
    leaderboard = pd.DataFrame(columns=["Boy", "Girl", "Score"])

# Function to generate love score
def calculate_love_score():
    return random.randint(50, 100)

# Function to determine love language
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

# UI Design
st.markdown("<h1 style='text-align: center; color: red;'>💘 Valentine's Day Love Calculator 💘</h1>", unsafe_allow_html=True)

# User input for names
col1, col2 = st.columns(2)
with col1:
    boy_name = st.text_input("Enter Boy's Name", placeholder="E.g. Alex")
with col2:
    girl_name = st.text_input("Enter Girl's Name", placeholder="E.g. Emily")

# Upload images
st.markdown("### Upload Images:")
boy_image = st.file_uploader("Upload Boy's Image", type=["jpg", "png", "jpeg"])
girl_image = st.file_uploader("Upload Girl's Image", type=["jpg", "png", "jpeg"])

# Love Score Calculation
if st.button("💞 Calculate Love Score 💞"):
    if boy_image and girl_image and boy_name and girl_name:
        with st.spinner("Calculating love score... 💕"):
            time.sleep(2)

        love_score = calculate_love_score()
        love_language = get_love_language(love_score)

        # Store result in leaderboard
        new_entry = pd.DataFrame([[boy_name, girl_name, love_score]], columns=["Boy", "Girl", "Score"])
        leaderboard = pd.concat([leaderboard, new_entry], ignore_index=True)
        leaderboard = leaderboard.sort_values(by="Score", ascending=False)

        # Save to CSV
        leaderboard.to_csv(LEADERBOARD_FILE, index=False)

        # Display images
        st.markdown("### 💑 Uploaded Images:")
        col1, col2 = st.columns(2)
        with col1:
            st.image(Image.open(boy_image).resize((250, 250)), caption=f"💙 {boy_name}")
        with col2:
            st.image(Image.open(girl_image).resize((250, 250)), caption=f"💖 {girl_name}")

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
        st.warning("Please enter both names and upload images to calculate the love score!")

# Leaderboard Section
st.markdown("---")
st.markdown("<h2 style='text-align: center; color: red;'>🔥 Love Leaderboard 🔥</h2>", unsafe_allow_html=True)

# Show leaderboard
if not leaderboard.empty:
    leaderboard.index += 1  # Start index from 1
    st.table(leaderboard)
else:
    st.markdown("<h4 style='text-align: center; color: gray;'>No results yet. Be the first! 💑</h4>", unsafe_allow_html=True)
