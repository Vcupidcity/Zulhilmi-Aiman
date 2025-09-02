import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("🚀 My First Streamlit App")

# User input
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, **{name}**! 👋")

# Slider
number = st.slider("Pick a number:", 1, 100, 25)
st.write(f"You selected: {number}")

# Random chart
st.subheader("Random Data Chart")
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(data)
