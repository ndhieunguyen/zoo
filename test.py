import streamlit as st

# Define the initial position and velocity of the object
x = 50
y = 50
vx = 100
vy = 100

# Define the size and color of the object
size = 30
color = "red"

# Define the CSS style for the object
style = f"""
position: absolute; 
left: {x}px; top: {y}px; 
width: {size}px; height: {size}px; 
background-color: {color}; 
animation: move {1/2}s linear infinite;
"""

# Define the CSS animation for the object
animation = f"""
@keyframes move {{ 0% {{ left: {x}px; top: {y}px; }} 100% {{ left: {x+vx}px; top: {y+vy}px; }} }}
"""

# Add the CSS style and animation to the HTML head
st.write(f"<head><style>{animation}</style></head>", unsafe_allow_html=True)

# Add the object to the HTML body
st.write(f'<div style="{style}"></div>', unsafe_allow_html=True)
