import streamlit as st
import pandas as pd

st.header("Uploading data")
uploaded_file = st.file_uploader("Upload data here!")

if uploaded_file is None:
    st.write("Did not upload a file yet")
    st.stop()

st.write(f"Thank you for uploading `{uploaded_file.name}`!")

data = pd.read_csv(uploaded_file)
st.write(data)
