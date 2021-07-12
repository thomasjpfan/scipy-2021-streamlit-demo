from pathlib import Path

import streamlit as st
import pandas as pd
import hiplot as hip


@st.cache
def load_data():
    return pd.read_csv(Path("media") / "ames_gbrt_search_results.csv")


@st.cache
def get_experiment(cv_results):
    xp = hip.Experiment.from_dataframe(
        cv_results[['mean_test_score', 'learning_rate',
                    'max_leaf_nodes', 'max_bins', 'mean_fit_time',
                    'mean_score_time']])
    return xp.to_streamlit(key="hip")


st.title("AMES House Price Prediction Hyperparameter Search Viz")
st.subheader("With `sklearn.ensemble.HistGradientBoostingRegressor`")
cv_results = load_data()
return_values = get_experiment(cv_results).display()
