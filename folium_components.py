import streamlit as st
from streamlit_folium import folium_static
import folium

st.title("SciPy 2019 🐍")
coord = [30.281928, -97.740345]

m = folium.Map(location=coord, zoom_start=16)
folium.Marker(
    coord, popup="SciPy 2019", tooltip="SciPy 2019"
).add_to(m)

folium_static(m)
