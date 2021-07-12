from pathlib import Path
import streamlit as st
import plotly.express as px
import pandas as pd

media_dir = Path("media")


@st.cache
def load_data():
    penguins_path = media_dir / "penguins.csv"
    return pd.read_csv(penguins_path)


penguins = load_data()
numerical_features = [
    'culmen_length_mm', 'culmen_depth_mm',
    'flipper_length_mm', 'body_mass_g']

feature = st.sidebar.radio("Select a feature", numerical_features)

st.header("EDA for penguins dataset!")

left, right = st.beta_columns(2)
with left:
    st.subheader(f"Slice of data for `{feature}`")
    st.write(penguins[['species', feature]])
with right:
    st.image(str(media_dir / "gentoo.jpeg"))


st.subheader(f"Histogram for `{feature}`")
hist = px.histogram(penguins,
                    x=feature,
                    color='species')
st.write(hist)
