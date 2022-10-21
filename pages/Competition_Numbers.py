
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
meetState = st.sidebar.multiselect("State",options=(['NSW' ,'QLD' ,'WA', 'VIC' ,'ACT' , 'SA' ,'TAS']))
if len(meetState) == 0:
    meetState = df['MeetState']
    
col1, col2,col4,col5 = st.columns(4)
with col1:
    st.sidebar.multiselect("State",options=(['NSW' ,'QLD' ,'WA', 'VIC' ,'ACT' , 'SA' ,'TAS']))
    #if len(col1) == 0:
    #    col1 = df['MeetState']
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
st.header('Competition Numbers - You can group by State or Year')
meetName = st.sidebar.multiselect("Meet Name",options=df['MeetName'].unique())
if len(meetName) == 0:
    meetName = df['MeetName']
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
df_exec = df.query(
   "Sex==@sex_input &  WeightClassKg==@weight_input & Equipment == @equpped & MeetState == @meetState & MeetName == @meetName & Event == @eventy"
)

df_exec['count'] = df_exec.groupby('MeetState')['MeetState'].transform('count')
df1 =df_exec[['MeetName', 'MeetState', 'MeetTown','count']]
#How many lifters, genders, weights, lifts, ----------------5/10
st.dataframe(df1,width=20000)
st.metric('Test',value=str(col1))
#Failed Lifts % Breakdown ---------------8/10 

#Number of lifters who went 9/9--------------------6/10

#BW Stats -------------------- 0/10
