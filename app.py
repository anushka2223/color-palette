import random
import streamlit as st
from mood_palette import mood_color_data, categorized_moods
from utils import render_palette

st.set_page_config(page_title="Color Palette AI", layout="centered")

st.markdown("""
    <h1 style='text-align: center;'>🎨 Mood & Theme-Based Color Palette AI</h1>
    <p style='text-align: center; color: gray;'>Choose a mood category and theme to get a perfect color palette!</p>
""", unsafe_allow_html=True)

# 🎲 Step 2: Surprise Me Button
if st.button("🎲 Surprise Me"):
    category = random.choice(list(categorized_moods.keys()))
    theme = random.choice(categorized_moods[category])
    st.success(f"Randomly selected: {category} → {theme}")
    colors = mood_color_data.get(theme)
    if colors:
        st.markdown("### 🎨 Suggested Color Palette")
        render_palette(colors)
    else:
        st.warning("No palette found for the selected theme.")
    st.stop()  # prevent dropdowns from showing when random is used

# Step 1: Manual Selection - Mood Category
category = st.selectbox("Choose a mood category:", list(categorized_moods.keys()))

# Step 3: Theme selection within selected category
themes = categorized_moods[category]
theme = st.selectbox("Choose a theme:", themes)

# Step 4: Show Palette
colors = mood_color_data.get(theme)
if colors:
    st.markdown("### 🎨 Suggested Color Palette")
    render_palette(colors)
else:
    st.warning("No palette found for the selected theme.")
