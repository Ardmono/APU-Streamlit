from multiprocessing.spawn import set_executable
from time import strptime
import pandas as pd 
import streamlit as st
from datetime import datetime
import time
import numpy as np


df = 'https://raw.githubusercontent.com/Ardmono/APU-Streamlit/main/filename.csv'
df = pd.read_csv(df)
df = df.drop(columns=['Age', 'Team', 'BirthYear', 'BirthDate','Country','State','Place','meetid','MeetCountry'])
df['Year'] = pd.DatetimeIndex(df['Date']).year
df.fillna(0, inplace=True)



#st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
#st.metric('Best Bench', value, delta=None, delta_color="normal", help=None)

b = 0
d = 0
s = 0



col1, col2, col3 = st.columns(3)
col1.metric(str(b), "70 °F", "1.2 °F")
col2.metric(str(d), "9 mph", "-8%")
col3.metric(str(s), "86%", "4%")

bodyweight = st.number_input("Bodyweight")
sex = st.select_slider("Sex", options=['Male', 'Female'])
benchtotal = st.number_input("Bench Best")
deadlift = st.number_input("Deadlift Best")
squat = st.number_input("Squat Best")
