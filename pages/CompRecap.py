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

df1 = df1[df1['Event'] == 'SBD']
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
            result.append(0)
    #print(listy[i]+'fail')
    df1[listy[i]+'fail'] = result
    df1[listy[i]+'fail'] = df1[listy[i]+'fail'].abs()
 

# task = df1['WeightClassKg'].unique()

# rslt_df = df1.loc[df1['WeightClassKg'] == 57]
# col4, col1, col2,col3 = st.columns(4)
# col4.metric("Weight Class",task[i])
# col1.metric("Bench", (rslt_df[rslt_df['Bench3Kgfail' > 0]].count()))
# col2.metric("Deadlift", (rslt_df['Deadlift3Kgfail'].count()))
# col3.metric('Squat',(rslt_df['Squat3Kgfail'].count()))
# # result = []

rsf = df1.loc[df1['WeightClassKg'] == 57]
print(len(df1.query('Bench3Kgfail > 0')))
# for value in df1["Squat1Kg"]:
#     if value > 0:
#         result.append(0)
#     elif value < 0:
#         result.append(value)
st.dataframe(df1,use_container_width=True,height=1200)


task = df1['WeightClassKg'].unique()
#print(task)
for i in range(len(task)):
    #print(task[i])
    rslt_df = df1.loc[df1['WeightClassKg'] == task[i]]
    #print(rslt_df)
    col4, col1, col2,col3 = st.columns(4)
    col4.metric("Weight Class",task[i])
    col1.metric("Bench", (rslt_df['Bench3Kgfail'].count()))
    col2.metric("Deadlift", (rslt_df['Deadlift3Kgfail'].count()))
    col3.metric('Squat',(rslt_df['Squat3Kgfail'].count()))
    
    

#df1['Squat3Kgfail'] = df1['Squat3Kgfail'].abs()
#df1['Squat3Kgfail'].apply(abs)
#print(df1['Squat3Kgfail'])
#df["Result"] = result  
#print(df)
##df1 = df1.drop(columns=['Division', 'Equipment', 'Federation', 'Date','MeetState','MeetTown','MeetName','Name','Event','Year'])
#print(df1)
#df1.lt(0).sum()


#How many lifters, genders, weights, lifts, 

#Failed Lifts % Breakdown

#Number of lifters who went 9/9

#BW Stats 
