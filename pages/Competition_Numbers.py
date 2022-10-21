
from time import strptime
import pandas as pd 
import streamlit as st
from datetime import datetime
import time
import numpy as np
import plotly.graph_objects as go

st.set_page_config(layout="wide")

df = 'https://raw.githubusercontent.com/Ardmono/APU-Streamlit/main/filename.csv'
df = pd.read_csv(df)
df = df.drop(columns=['Age', 'Team', 'BirthYear', 'BirthDate','Country','State','MeetCountry'])
df['Year'] = pd.DatetimeIndex(df['Date']).year
#df.fillna(0, inplace=True)
df1 = df

st.title('Competition Numbers - You can filter & group by State, Town or Year')
 
df = df1
# meetState = st.sidebar.multiselect("Filter State",options=(['NSW' ,'QLD' ,'WA', 'VIC' ,'ACT' , 'SA' ,'TAS']),default='NSW')
# if len(meetState) == 0:
#     meetState = df['MeetState']

st.header('Filter by')
col1, col2, col3 = st.columns(3)
with col1:
    meetState =st.multiselect("Filter Statey",options=(['NSW' ,'QLD' ,'WA', 'VIC' ,'ACT' , 'SA' ,'TAS']))
    if len(meetState) == 0:
        meetState = df['MeetState']
with col2:
    meetTown = st.multiselect("Meet Town",options=df['MeetTown'].unique())
    if len(meetTown) == 0:
        meetTown = df['MeetTown']
with col3:
    yer = st.multiselect("Year",options=df['Year'].unique())
    if len(yer) == 0:
        yer = df['Year']
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
eventy = st.sidebar.radio("Event",options=('All','SBD', 'B', 'BD', 'D'))
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
equpped = st.sidebar.radio("Equipment",options =("All","Raw","Single-ply"))
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
   "Sex==@sex_input &  WeightClassKg==@weight_input & Equipment == @equpped & MeetState == @meetState & MeetName == @meetName & Event == @eventy & MeetTown == @meetTown & Year == @yer"
)


print(df_exec)
df_exec['count'] = df_exec.groupby('meetid')['meetid'].transform('count')
df1 =df_exec[['MeetName', 'MeetState', 'MeetTown','Year','count']]
#How many lifters, genders, weights, lifts, ----------------5/10

df1.drop_duplicates(subset="MeetName",
                     keep='first', inplace=True)

county = len(df1.index)
bleh = county
county = int(county) * 42
st.dataframe(df1,width=20000,height=county)
print(col1)
st.metric('Test',value=str(col1))
st.text(bleh)
st.text(county)
#Failed Lifts % Breakdown ---------------8/10 

#Number of lifters who went 9/9--------------------6/10

#BW Stats -------------------- 0/10
