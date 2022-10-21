
from time import strptime
import pandas as pd 
import streamlit as st
from datetime import datetime
import time
import numpy as np
import plotly.graph_objects as go



df = 'https://raw.githubusercontent.com/Ardmono/APU-Streamlit/main/filename.csv'
df = pd.read_csv(df)
df = df.drop(columns=['Age', 'Team', 'BirthYear', 'BirthDate','Country','State','meetid','MeetCountry'])
df['Year'] = pd.DatetimeIndex(df['Date']).year
#df.fillna(0, inplace=True)
df1 = df


 
df = df1
meetName = st.sidebar.multiselect("State",options=('NSW' ,'QLD' ,'WA', 'VIC' ,'ACT' , 'SA' ,'TAS'))
if len(meetName) == 0:
    meetName = df['MeetName']
    
col1, col2,col4,col5 = st.columns(4)
with col1:
    st.selectbox("City", ["City1", "City2"])
with col2:
    st.selectbox("District", ["District1", "District2"])
with col4:
    st.selectbox("c", ["c", "c"])
with col5:
    st.selectbox("B", ["b", "b"])



sex_input = st.sidebar.radio("Sex",options =("All","M","F"))
if sex_input == 'All':
    sex_input = df['Sex']
eventy = st.sidebar.radio("Event",options=('SBD', 'B', 'BD', 'D','All'))
#if len(eventy) == 0:
#    eventy = 'SBD'
if eventy == 'All':
    eventy = df['Event']
st.header('Competition Recap, defaults is latest comp ')
maxmeet = max(df.MeetName.apply(len))
meeter = meetName
if len(meeter) > maxmeet+1 :
    meeter = 'All Comps'

weight_input = st.sidebar.multiselect("Weight Class",options=df['WeightClassKg'].unique())
if len(weight_input) == 0:
    weight_input = df['WeightClassKg']
equpped = st.sidebar.radio("Equipment",options =("Raw","Single-ply","All"))
if equpped == 'All':
    equpped = df['Equipment']
wheres = st.sidebar.radio(label="Comp Type - Does not work, unsure how to fix, disabling until can figure out resolution - Likely need to import ALL current APU State/National records and use that ",options =("All","State","National"),disabled=True)
if wheres == 'All':
    wheres = df['MeetName']
elif wheres == 'State':
    wheres = df['MeetName'] # Need to subsect for keyword "State" 
elif wheres == 'State':
    wheres = df['MeetName'] # Need to subsect for keyword "National"
else:
    wheres = df['MeetName']
    
# state = st.sidebar.multiselect("State",options=('NSW' ,'QLD' ,'WA', 'VIC' ,'ACT' , 'SA' ,'TAS'))
# if len(state) == 0:
#     state = df['MeetState']
#print(df1.iloc[:,26:35])
# df_exec = df.query(
#    "Sex==@sex_input &  WeightClassKg==@weight_input & Equipment == @equpped & MeetState == @state & MeetName == @meetName & Event == @eventy"
# )

# #df_filtered = df_exec.query(len('Squat1Kg > 0 & Squat2Kg > 0 & Squat3Kg > 0'))
# #['Squat1Kg' , 'Squat2Kg'  ,'Squat3Kg' ,  'Bench1Kg',  'Bench2Kg' ,'Bench3Kg',  'Deadlift1Kg',  'Deadlift2Kg', 'Deadlift3Kg']
# #st.metric('All good squats', value=len(df_exec.query('Sex == 'F'')), delta=None, delta_color="normal", help=None)
# dfsex = df.query(
#    "WeightClassKg==@weight_input & Equipment == @equpped & MeetState == @state & MeetName == @meetName & Event == @eventy"
# )


# lifters = len(dfsex[dfsex['Sex'] =='F']) + len(dfsex[dfsex['Sex'] =='M'])
# #print(lifters)
# #print(df_exec[df_exec['Sex'] =='F'].count())
# #st.metric('All good squats', value=len(df_exec.query('Sex == 'M'')), delta=None, delta_color="normal", help=None)
# # st.metric(label="Count of failed Bench3",value=len(df_exec.query('Bench3Kgfail > 0')))
# a, b,c = st.columns(3,gap='Small')
# a.metric(label="Female Lifters", value=len(dfsex[df['Sex'] =='F']))
# b.metric(label="Male Lifters", value=len(dfsex[df['Sex'] =='M']))
# c.metric(label="Total Lifters", value=lifters)
# #d.metric(label="Total KG of all lifted weights", value=(str(df_exec['TotalKg'].sum())+' Kg'))
# st.text('Current Comp: '+str(meeter))
# col1, col2, col3,col4,col5 = st.columns(5,gap='Medium')
# col1.metric(label="How Many Lifters", value=len(df_exec.query('Bench3Kgfail > 0')))
# col2.metric(label="Gender Ratios", value='Bleh')
# col3.metric(label="% Succesful Lifts", value='Bleh')
# col4.metric(label="Total KG of all lifted weights", value=(str(df_exec['TotalKg'].sum())+' Kg'))
# col5.metric(label="Count of 9/9 Lifts",value=len(df_exec.query('Squat3Kg > 1 & Squat2Kg > 1 & Squat1Kg > 1 & Bench1Kg > 1 & Bench2Kg > 1 & Bench3Kg > 1 & Deadlift1Kg > 1 & Deadlift2Kg > 1 & Deadlift3Kg > 1')))




#How many lifters, genders, weights, lifts, ----------------5/10

#Failed Lifts % Breakdown ---------------8/10 

#Number of lifters who went 9/9--------------------6/10

#BW Stats -------------------- 0/10
