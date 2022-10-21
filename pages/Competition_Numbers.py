
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

st.title('Competition Numbers - You can group by State or Year')
 
df = df1
# meetState = st.sidebar.multiselect("Filter State",options=(['NSW' ,'QLD' ,'WA', 'VIC' ,'ACT' , 'SA' ,'TAS']),default='NSW')
# if len(meetState) == 0:
#     meetState = df['MeetState']

st.header('Filter by')
col1, col2 = st.columns(2)
with col1:
    meetState =st.multiselect("Filter Statey",options=(['NSW' ,'QLD' ,'WA', 'VIC' ,'ACT' , 'SA' ,'TAS']))
    #if len(col1) == 0:
    #    col1 = df['MeetState']
    if len(meetState) == 0:
        meetState = df['MeetState']
with col2:
    meetTown = st.multiselect("Meet Town",options=df['MeetTown'].unique())
    if len(meetTown) == 0:
        meetTown = df['MeetTown']
    #st.selectbox("Filter District", ["District1", "District2"])
# with col4:
#     st.selectbox("Filter c", ["c", "c"])
# with col5:
#     st.selectbox("Filter B", ["b", "b"])

st.header('Group by')
a, b,c,d = st.columns(4)
with a:
    st.multiselect("Statey",options=(['NSW' ,'QLD' ,'WA', 'VIC' ,'ACT' , 'SA' ,'TAS']))
    #if len(col1) == 0:
    #    col1 = df['MeetState']
with b:
    st.selectbox("District", ["District1", "District2"])
with c:
    st.selectbox("c", ["c", "c"])
with d:
    st.selectbox("B", ["b", "b"])



sex_input = st.sidebar.radio("Sex",options =("All","M","F"))
if sex_input == 'All':
    sex_input = df['Sex']
eventy = st.sidebar.radio("Event",options=('SBD', 'B', 'BD', 'D','All'))
#if len(eventy) == 0:
#    eventy = 'SBD'
if eventy == 'All':
    eventy = df['Event']

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

df1.drop_duplicates(subset="MeetName",
                     keep='first', inplace=True)

st.dataframe(df1,width=20000)
print(col1)
st.metric('Test',value=str(col1))
#Failed Lifts % Breakdown ---------------8/10 

#Number of lifters who went 9/9--------------------6/10

#BW Stats -------------------- 0/10
