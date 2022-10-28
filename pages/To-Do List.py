from time import strptime
import pandas as pd 
import streamlit as st
from datetime import datetime
import time
import numpy as np
import plotly.graph_objects as go



df = 'https://raw.githubusercontent.com/Ardmono/APU-Streamlit/main/filename.csv'
df = pd.read_csv(df)
dfx = df

#print(df)

#len(df.query('MeetName < 1'))
print(df[['MeetName', 'MeetState', 'MeetTown']])
df.fillna(value='Unknown',inplace=True)

print(df[['MeetName', 'MeetState', 'MeetTown']])

#nan_in_col  = df[df['MeetName'].isna()]
df1 = df[(df.MeetState == 'Unknown') | (df.MeetTown == 'Unknown') | (df.MeetTown == 0) | (df.MeetTown == 'UNK')  | (df.MeetState == 'Unknown')]  #& (df.MeetName == 0)]

#,'Bench1Kg', 'Bench2Kg', 'Bench3Kg' ,'Best3BenchKg' ,'Deadlift1Kg', 'Deadlift2Kg' ,'Deadlift3Kg', 'Best3DeadliftKg'
df1 = df1.drop(columns=['Age', 'Team', 'BirthYear', 'BirthDate','Country','State','Place','Name', 'WeightClassKg', 'BodyweightKg', 'Division', 'Squat1Kg', 'Squat2Kg', 'Squat3Kg', 'Best3SquatKg','Bench1Kg', 'Bench2Kg', 'Bench3Kg' ,'Best3BenchKg' ,'Deadlift1Kg', 'Deadlift2Kg' ,'Deadlift3Kg', 'Best3DeadliftKg','TotalKg'])
##a = df.query('a.isnull()', engine='python')
df1.drop_duplicates(subset="meetid",
                     keep='first', inplace=True)

st.text('Records with missing or unknown data')
st.metric('Records to correct',value=len(df1['meetid'].unique()))
#print(df1['meetid'])

st.dataframe(df1,width=20000)

task = ['Wilks Score', 'Dots', 'Year Fix', 'Style','Page','BestLift','Records']

st.header('To do')
for i in range(len(task)):
  st.checkbox(label=(task[i]))
  print(st.checkbox)
if st.checkbox(label='Remove Floats'):
    value=True
    
    

df2 = dfx[(df.Sex != 'M') & (dfx.Sex != 'F')]
df2 =df2[['Sex', 'MeetTown']]
#st.dataframe(df2,width=2000)
print(df2)