import pandas as pd
from PIL import Image
import pandas_datareader as web
import datetime as dt
import numpy as np
import streamlit as st
 
 
image = Image.open('logo.jpeg')

st.image(image, width = 700)
 
st.title('Cryptocurrency Prediction.')
 
 
with st.form(key='my_form'):
    crypto=st.selectbox('Bitcoin', ['BTC'])
    start=st.date_input('Start')
    end=st.date_input('End')
    submit_button = st.form_submit_button(label='Submit')
 
if submit_button:
    df = web.DataReader(f'{crypto}-USD', 'yahoo', start, end)
    df
    st.line_chart(df['Adj Close'])