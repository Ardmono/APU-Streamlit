from time import strptime
import pandas as pd 
import streamlit as st
from datetime import datetime
import time
import numpy as np


df = 'https://raw.githubusercontent.com/Ardmono/APU-Streamlit/main/filename.csv'
df = pd.read_csv(df)
df = df.drop(columns=['Age', 'Team', 'BirthYear', 'BirthDate','Country','State','Place','Equipment','meetid','MeetCountry'])
df['Year'] = pd.DatetimeIndex(df['Date']).year
df.fillna(0, inplace=True)

task = df['WeightClassKg'].unique()
#print(task)
for i in range(len(task)):
    #print(task[i])
    rslt_df = df.loc[df['WeightClassKg'] == task[i]]
    print(rslt_df)
    col4, col1, col2,col3 = st.columns(4)
    col4.metric("Weight Class",task[i],"1.2f")
    col1.metric("Bench", (rslt_df['Best3BenchKg'].max()), "1.2 °F")
    col2.metric("Wind", (rslt_df['Best3DeadliftKg'].max()), "-8%")
    col3.metric('Squat',(rslt_df['Best3SquartKg'].max()),'5')

#print(df['WeightClassKg']=57.max)
# maxClm = df['Best3BenchKg'].max()
# #print(maxClm)
# rslt_df = df.loc[df['WeightClassKg'] == task[i]]
#print(rslt_df['Best3BenchKg'].max())
#where weightclass = I = bestbench
# for i in range(len(task)):
# col4, col1, col2, col3 = st.columns(3)
# col1.metric("Temperature", "70 °F", "1.2 °F")
# col2.metric("Wind", "9 mph", "-8%")
# col3.metric("Humidity", "86%", "4%")
# col4.metric("Humidity", "86%", "4%")

#for i in range(len(task)):
#  st.checkbox(label=(task[i]))

# col1, col2, col3 = st.columns(3)
# col1.metric("Temperature", "70 °F", "1.2 °F")
# col2.metric("Wind", "9 mph", "-8%")
# col3.metric("Humidity", "86%", "4%")