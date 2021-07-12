import os
import streamlit as st

penguin = st.radio(
    "Select a penguin",
    options=["adelie", "gentoo", "chinstrap"])

st.header(f"Here is a {penguin}!")

image_path = os.path.join("media", f"{penguin}.jpeg")
st.image(image_path)
