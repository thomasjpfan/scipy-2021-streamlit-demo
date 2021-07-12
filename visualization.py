from pathlib import Path
import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px
import altair as alt


st.title("EDA for penguins dataset!")

penguins_path = Path("media") / "penguins.csv"
penguins = pd.read_csv(penguins_path)
st.write(penguins)


# Matplotlib + pandas
st.header("How many penguins of each species are in our dataset?")
counts = penguins['species'].value_counts()

count_ax = counts.plot.bar(color=['blue', 'red', 'green'])
st.write(count_ax.figure)


# Seaborn
st.header("Can flipper length be used to distingushed the species?")

flipper_fig = sns.displot(penguins,
                          x='flipper_length_mm',
                          hue='species',
                          kind='kde')
st.write(flipper_fig.fig)


st.header("Is the culmen length/depth useful for classifying species?")

scat = px.scatter(penguins,
                  x="culmen_length_mm",
                  y="culmen_depth_mm",
                  marginal_y="violin",
                  marginal_x='box',
                  color='species')
st.write(scat)


st.header("How is the body mass for each species distributed?")
hist = alt.Chart(penguins, width=600, height=200).mark_boxplot().encode(
    x="body_mass_g:Q",
    y="species:N",
    color='species:N',
)
st.write(hist)
