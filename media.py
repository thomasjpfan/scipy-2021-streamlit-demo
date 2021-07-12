from pathlib import Path

import streamlit as st

media_dir = Path("media")

st.header("Displaying an image")
st.image(str(media_dir / "gentoo.jpeg"))

st.header("Displaying audio")
st.audio(str(media_dir / "penguin-noise.mp3"))

st.header("Displaying video")
st.video(str(media_dir / "penguin-video.mp4"))
