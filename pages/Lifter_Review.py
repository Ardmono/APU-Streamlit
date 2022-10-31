from time import strptime
import pandas as pd 
import streamlit as st
from datetime import datetime
import time
import numpy as np
import plotly.express as px
import plotly

df = 'https://raw.githubusercontent.com/Ardmono/APU-Streamlit/main/filename.csv'
df = pd.read_csv(df)
df = df.drop(columns=['Age', 'Team', 'BirthYear', 'BirthDate','Country','State','Place','MeetCountry'])
df['Year'] = pd.DatetimeIndex(df['Date']).year
df.fillna(0, inplace=True)

#df['Date'] = pd.to_datetime(df['Date'])

#Years/comps in review for athletes 

lifteroptions = df['Name'].unique().tolist()
#dateoptions = df['Date'].unique()#.tolist()

liftername = st.selectbox('What is the listers name', lifteroptions, 100)
liftername = 'Louise Sutton'
# liftername = st.multiselect("Lifter Name",options=df['Name'].unique())
# if len(liftername) == 0:
#     liftername = df['Name']

df = df[df['Name'] == liftername]
maxipfgl = df['IPFGL'].max()
maxipfgl = int(maxipfgl)
maxipfgl = maxipfgl + 10
dateoptions = df['Date'].unique().tolist()
print(dateoptions)
fig2 = px.bar(df, x='Name', y=['Best3SquatKg', 'Best3BenchKg'], animation_frame=dateoptions, range_y=[0,maxipfgl])



fig2.update_layout(width=500)


st.write(fig2)
#print(df['Name'].value_counts())

# Max Bristow, Abbas Pordel
#print(df)
#print(df[df['Name'] == 'Louise Sutton'])
