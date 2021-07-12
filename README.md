# Light Up Your Data with Streamlit! (Scipy 2021)

- [Link to slides](https://thomasjpfan.github.io/scipy-2021-streamlit)

This repo contains all the material used for my Scipy 2021 talk on Streamlit. The hosted version on Streamlit Sharing is a dashboard explaining a machine learning model's predictions using SHAP and Anchor explanations. The source of this dashboard is in `explain.py`: [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/thomasjpfan/scipy-2021-streamlit-demo/main/explain.py)

## Installation instructions

0. Clone repo and go into folder:

```
git clone https://github.com/thomasjpfan/scipy-2021-streamlit-demo
cd scipy-2021-streamlit-demo
```

1. Create a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements-all.txt
```

3. Run streamlit on any of the python files. For example:

```bash
streamlit run explain.py
```

## License

This repo is under the [MIT License](LICENSE).
