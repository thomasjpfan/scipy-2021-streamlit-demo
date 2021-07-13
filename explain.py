from pathlib import Path

import joblib
import pandas as pd
import shap
from anchor.anchor_tabular import AnchorTabularExplainer
import numpy as np
import streamlit as st
import streamlit.components.v1 as componenets
st.set_page_config(initial_sidebar_state="expanded")


###########
# Load Data
###########
media_dir = Path("media")
categorical_columns = ["island", "gender"]
numerical_columns = [
    "culmen_length_mm", "culmen_depth_mm",
    "flipper_length_mm", "body_mass_g"]
feature_names = categorical_columns + numerical_columns


@st.cache
def load_data():
    penguins = pd.read_csv(media_dir / "penguins.csv")
    return penguins[feature_names], penguins["species"]


X, y = load_data()


############
# User input
############
st.sidebar.subheader("Select your Penguin")

island_categories = ["Biscoe", "Dream", "Torgersen"]
gender_categories = ["FEMALE", "MALE"]
island = st.sidebar.radio("Select an island",
                          island_categories)
gender = st.sidebar.selectbox("Select a gender",
                              gender_categories)
culmen_length_mm = st.sidebar.number_input(
    "Select culmen length (mm)",
    min_value=32, max_value=60, value=44, step=5)
culmen_depth_mm = st.sidebar.number_input(
    "Select culmen depth (mm)",
    min_value=13, max_value=22, value=17, step=2)
flipper_length_mm = st.sidebar.number_input(
    "Select flipper length (mm)",
    min_value=172, max_value=231, value=197, step=10)
body_mass_g = st.sidebar.number_input(
    "Select body mass (g)",
    min_value=2700, max_value=6300, value=4050, step=500)

user_input = [[island, gender, culmen_length_mm,
               culmen_depth_mm, flipper_length_mm,
               body_mass_g]]
user_df = pd.DataFrame(user_input, columns=feature_names)

##############################
# Load Model & make prediction
##############################
clf = joblib.load(media_dir / "penguin_clf.joblib")
class_names = clf.classes_
prediction = clf.predict(user_df)[0]

#################
# Make Prediction
#################
st.sidebar.write(f"## Prediction: {prediction}")

proba = clf.predict_proba(user_df)
proba_df = pd.DataFrame(proba, columns=class_names)
st.sidebar.write(proba_df)


###################
# Explain with SHAP
###################
st.write(f"## Explanation for Predicting: **{prediction}**")
st.header("SHAP values")

user_encoded = clf[:-1].transform(user_df)
explainer = shap.TreeExplainer(clf[-1])
shap_values = explainer.shap_values(
    user_encoded[[0], :], check_additivity=False)

shap_plot_reprs = [
    shap.force_plot(
        explainer.expected_value[i], shap_values[i],
        user_encoded,
        feature_names=feature_names,
        out_names=class_names[i],
    )._repr_html_()
    for i in range(3)
]
shap_html_repr = "".join(shap_plot_reprs)

componenets.html(f"<head>{shap.getjs()}</head>{shap_html_repr}", height=420)


######################
# Explain with Anchors
######################
@st.cache
def get_anchor_explainer():
    X_encoded = clf[:-1].transform(X)
    return AnchorTabularExplainer(
        class_names,
        feature_names,
        X_encoded,
        categorical_names={
            0: island_categories,
            1: gender_categories,
        },
    )


anchor_explainer = get_anchor_explainer()
st.header("Anchors")
class_to_idx = {
    name: idx
    for idx, name in enumerate(clf[-1].classes_)
}


def predict(X):
    predicted_class = clf[-1].predict(X)[0]
    return np.array([class_to_idx[predicted_class]],
                    dtype=np.int32)


exp = anchor_explainer.explain_instance(
    user_encoded[0, :], predict)
componenets.html(exp.as_html(), height=700)
