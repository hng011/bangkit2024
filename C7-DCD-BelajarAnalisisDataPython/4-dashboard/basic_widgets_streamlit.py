import streamlit as st
import datetime
import pandas as pd

# Text input
name = st.text_input(label="Full Name", value='')
st.write("Name:",name)

### Input Widget
# Text area
text = st.text_area("Feedback")
st.write("Your feedback:",text)

# Number input
number = st.number_input(label="Age")
st.write(f"Age: {number} Y.O.")

# Date Input
date = st.date_input(label="Date of Birth", min_value=datetime.date(1990,1, 1))
st.write("Date of Birth:",date)

# File Uploader
upload_file = st.file_uploader("Choose a CSV file")
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)


### Button Widget
# Button
if st.button("say hello"):
    st.write("Hello, there!")

# Checkbox
st.write("Check this if you want to use camera")
agree = st.checkbox("I agree")
if agree:
    # camera input 
    picture = st.camera_input("Take a Pict")
    if picture:
        st.image(picture)

# Radio Button
genre = st.radio(
    label="Favorite movie genre",
    options=("comedey","action","drama"),
    horizontal=False
)

# select box
genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# Multi select
genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# Slider
values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)