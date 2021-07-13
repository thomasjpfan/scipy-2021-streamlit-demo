import streamlit as st
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(10, 4),
    columns=[f'col_{i}' for i in range(4)]
)

st.title("DataFrames!")
st.write("Show me the data")
st.write(data)
