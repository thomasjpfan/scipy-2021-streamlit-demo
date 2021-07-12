from pathlib import Path
import streamlit as st
import plotly.express as px
import pandas as pd

media_dir = Path("media")
penguins_path = media_dir / "penguins.csv"
penguins = pd.read_csv(penguins_path)

numerical_features = [
    'culmen_length_mm', 'culmen_depth_mm',
    'flipper_length_mm', 'body_mass_g']

feature = "body_mass_g"

st.header("EDA for penguins dataset!")
st.subheader(f"Slice of data for {feature}")
st.write(penguins[['species', feature]])
st.image(str(media_dir / "gentoo.jpeg"))


st.subheader(f"Histogram for {feature}")
hist = px.histogram(penguins,
                    x=feature,
                    color='species')
st.write(hist)
