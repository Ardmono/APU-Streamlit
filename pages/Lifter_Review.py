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
if len(liftername) > 0:
    df = df[df['Name'] == liftername]
    maxipfgl = df['TotalKg'].max()
    maxipfgl = int(maxipfgl)
    maxipfgl = maxipfgl + 10
    dateoptions = df['Date'].unique().tolist()
    print(dateoptions)
    text = df['Date'].unique().tolist()
    fig2 = px.bar(df, x='Name', y=['Best3BenchKg', 'Best3SquatKg', 'Best3DeadliftKg','TotalKg'], animation_frame=dateoptions, range_y=[0,maxipfgl],barmode='group',text_auto=True)

    for i, frame in enumerate(fig2.frames):
        frame.layout.title = "Avg Population: {}".format(text[i])
        
    for step in fig2.layout.sliders[0].steps:
        step["args"][1]["frame"]["redraw"] = True

        
    fig2.update_layout(width=800, height=800)
    st.write(fig2)
else:
    st.text('Pick someone')
#print(df['Name'].value_counts())

# Max Bristow, Abbas Pordel
#print(df)
#print(df[df['Name'] == 'Louise Sutton'])
