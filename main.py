import streamlit as st
import pandas as pd

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_training = st.beta_container()

with header:
    st.title('Welcome to my twitterscrapping project')
    st.text('WB studios twitter scrapping')

with dataset:
    twitterproject = pd.read_csv('data/twitterproject.csv')
    st.write(twitterproject.head())

with model_training:
    st.text('Enter time')
    st.text('Enter date')

    sel_col, disp_col = st.beta_columns(2)

    Time = sel_col.text_input('Time')
    Date = sel_col.text_input('Date')



