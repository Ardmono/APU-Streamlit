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
df1 = df
#df1 = df1.drop(columns=['Age', 'Team', 'BirthYear', 'BirthDate','Country','State','Place','meetid','MeetCountry'])

#df1['Squat1Fail'] = df1[df1['Squat1Kg'] < 0]
listy = ['Squat1Kg' , 'Squat2Kg'  ,'Squat3Kg' ,  'Bench1Kg',  'Bench2Kg' ,'Bench3Kg',  'Deadlift1Kg',  'Deadlift2Kg', 'Deadlift3Kg']
for i in range(len(listy)):
    #df1[listy[i]] = df[listy[i]]
    result = []
    v = 'fail'
    for value in df1[listy[i]]:
        if value > 0:
            result.append(0)
        elif value < 0:
            result.append(value)
        else:
            result.append('fail')
    #print(listy[i]+'fail')
    df1[listy[i]+'fail'] = result

# result = []
# for value in df1["Squat1Kg"]:
#     if value > 0:
#         result.append(0)
#     elif value < 0:
#         result.append(value)

st.dataframe(df1,use_container_width=True,height=1200)
     
#df["Result"] = result  
#print(df)
##df1 = df1.drop(columns=['Division', 'Equipment', 'Federation', 'Date','MeetState','MeetTown','MeetName','Name','Event','Year'])
print(df1)
#df1.lt(0).sum()


#How many lifters, genders, weights, lifts, 

#Failed Lifts % Breakdown

#Number of lifters who went 9/9

#BW Stats 
