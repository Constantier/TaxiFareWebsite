import streamlit as st
import requests
from datetime import datetime
import numpy as np
import pandas as pd

'''
# TaxiFareModel front
'''
url = 'https://taxifare.lewagon.ai/predict'

'''
Enter :
'''
CSS = """
h3 {
    color: orange;
}
"""
col1, col2, col3, col4 = st.columns(4)

with col1:
    date_input=st.date_input('Date',datetime.today())
    time_input = st.time_input('Time', datetime.today())

with col2:
    pickup_long = st.number_input('Pickup longitude', -73.985440)
    pickup_lat = st.number_input('Pickup latitude',40.748590)

with col3 :
    dropoff_long = st.number_input('Dropoff longitude', -73.985440)
    dropoff_lat = st.number_input('Dropoff latitude',40.748590)

with col4:
    pass_count=st.number_input('Number of passenger',1,8,1,1)

button=st.button('Predict Fare')
if button:
    print(str(date_input)+str(time_input))
    params={
        'pickup_datetime':str(date_input)+' '+str(time_input),
        'pickup_longitude':pickup_long,
        'pickup_latitude':pickup_lat,
        'dropoff_longitude':dropoff_long,
        'dropoff_latitude':dropoff_lat,
        'passenger_count':pass_count
    }
    rep=requests.get(url,params=params).json()
    st.markdown(f"### Predicted fare of ${round(rep['fare'],2)}")
    st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)
    st.markdown("![Alt Text](https://media1.giphy.com/media/14SAx6S02Io1ThOlOY/giphy.gif?cid=ecf05e47bqzrw6oixl94iiis8dlaor7pnduytptyuecy9ud1&rid=giphy.gif)")

df = pd.DataFrame(
     [[pickup_lat,pickup_long],[dropoff_lat,dropoff_long]],
     columns=['lat', 'lon'])

st.map(df,11,use_container_width=False)
