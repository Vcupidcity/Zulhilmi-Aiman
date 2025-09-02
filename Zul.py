import streamlit as st

# Title and subtitle
st.title("Hello Streamlit 👋")
st.subheader("This is a simple Streamlit app")

# Input text
name = st.text_input("Enter your name:")

# Button
if st.button("Greet Me"):
    st.success(f"Hello, {name}!") if name else st.warning("Please enter your name first.")

# Slider
age = st.slider("Select your age:", 0, 100, 18)
st.write(f"Your age is: {age}")
