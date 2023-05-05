import streamlit as st
import random
from src.animals import Zoo

zoo = Zoo("data.csv")
# for animal in zoo.animals:
for i in range(5):
    x = random.randint(0, 100)
    y = random.randint(0, 100)

    # Define the size and color of the object
    size = 30
    color = "red"

    # Define an HTML div with position: absolute to place the object at the desired coordinates
    st.write(
        f"""
        <div style="position: absolute; left: {x}px; top: {y}px;">
            <svg width="{size}" height="{size}">
                <circle cx="{size/2}" cy="{size/2}" r="{size/2}" fill="{color}" />
            </svg>
        </div>
        """,
        unsafe_allow_html=True,
    )
