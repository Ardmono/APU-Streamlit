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
sex_input = st.sidebar.radio("Sex",options =("All","M","F"))
if sex_input == 'All':
    sex_input = df['Sex']
st.header('Top Lifts by Weight Category - Filters for Equipped, State, National/State Lifts and Weight Category on the side')
weight_input = st.sidebar.multiselect("Weight Class",options=df['WeightClassKg'].unique())
if len(weight_input) == 0:
    weight_input = df['WeightClassKg']
equpped = st.sidebar.radio("Equipment",options =("All","Raw","Single-ply"))
if equpped == 'All':
    equpped = df['Equipment']
wheres = st.sidebar.radio("Comp Type",options =("All","State","National"))
if wheres == 'All':
    wheres = df['MeetName']
state = st.sidebar.multiselect("State",options=('NSW' ,'QLD' ,'WA', 'VIC' ,'ACT' , 'SA' ,'TAS'))
if len(state) == 0:
    state = df['MeetState']

df = df.query(
   "Sex==@sex_input & WeightClassKg==@weight_input & Year == @yer & MeetState == @meetState & MeetTown == @meetTown & MeetName == @meetName & Name == @liftername & Division == @divison"
)
#split the table into two - Men and Women 
task = df['WeightClassKg'].unique()
#print(task)
for i in range(len(task)):
    #print(task[i])
    rslt_df = df.loc[df['WeightClassKg'] == task[i]]
    print(rslt_df)
    col4, col1, col2,col3,col5 = st.columns(5)
    col4.metric("Weight Class",task[i])
    col1.metric("Bench", (rslt_df['Best3BenchKg'].max()))
    col2.metric("Deadlift", (rslt_df['Best3DeadliftKg'].max()))
    col3.metric('Squat',(rslt_df['Best3SquatKg'].max()))
    col5.metric('Total',(rslt_df['TotalKg'].max()))




# task = df['WeightClassKg'].unique()
# #print(task)
# for i in range(len(task)):
#     #print(task[i])
#     rslt_df = df.loc[df['WeightClassKg'] == task[i]]
#     print(rslt_df)
#     col4, col1, col2,col3,col5 = st.columns(5)
#     col4.metric("Weight Class",task[i])
#     col1.metric("Bench", (rslt_df['Best3BenchKg'].max()))
#     col2.metric("Deadlift", (rslt_df['Best3DeadliftKg'].max()))
#     col3.metric('Squat',(rslt_df['Best3SquatKg'].max()))
#     col5.metric('Total',(rslt_df['TotalKg'].max()))

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