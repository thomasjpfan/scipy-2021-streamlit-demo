import streamlit as st

##########
# checkbox
##########
st.header("`st.checkbox`")
agree = st.checkbox("I agree")

if agree:
    st.subheader("You agreed! 😃")
st.write("---")


##########
# radio
##########
st.header("`st.radio`")
species = st.radio(
    "What is your favorite pet?",
    ("cat", "dog", "snake", "fish")
)
st.subheader(f"Radio: **{species}**")
st.write("---")


###########
# selectbox
###########
st.header("`st.selectbox`")
option = st.selectbox(
    "What is your favorite pet?",
    ("cat", "dog", "snake", "fish")
)
st.subheader(f"Selectbox: **{option}**")
st.write("---")

#############
# multiselect
#############
st.header("`st.multiselect`")
options = st.multiselect(
    "What is your favorite pet?",
    ("cat", "dog", "snake", "fish")
)
st.subheader(f"Multiselect: **{options}**")
st.write("---")

########
# slider
########
st.header("`st.slider`")
value = st.slider(
    "Choose a value",
    min_value=0,
    max_value=100,
    step=1,
    value=50,
)
st.subheader(f"Slide selected: {value}")
st.write("---")


############
# date_input
############
st.header("`st.date_input`")
d = st.date_input("When's your birthday")
st.write('Your birthday is:', d)
st.write("---")

###########
# text_area
###########
st.header("`st.text_area`")
name = st.text_area(
    "What is your name?", "John Doe")
st.write(f"Your name is {name}")
