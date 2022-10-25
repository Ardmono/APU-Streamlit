
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
b,c,d = st.columns(3)
# with a:
#     st.multiselect("Statey",options=(['NSW' ,'QLD' ,'WA', 'VIC' ,'ACT' , 'SA' ,'TAS']))
#     #if len(col1) == 0:
#     #    col1 = df['MeetState']
with b:
    grpst = st.radio("Group by State: ", ["False", "True"])
with c:
    grpyr =st.radio("Group by Year: ", ["True", "False"])
with d:
    grpto =st.radio("Group by Town: ", ["True", "False"])



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

    
# state = st.sidebar.multiselect("State",options=('NSW' ,'QLD' ,'WA', 'VIC' ,'ACT' , 'SA' ,'TAS'))
# if len(state) == 0:
#     state = df['MeetState']
#print(df1.iloc[:,26:35])
df_exec = df.query(
   "Sex==@sex_input &  WeightClassKg==@weight_input & Equipment == @equpped & MeetState == @meetState & MeetName == @meetName & Event == @eventy & MeetTown == @meetTown & Year == @yer"
)


#grpyr
#grpto
#df_exec['State_Year'] = (df_exec[['MeetState']]+df_exec[['Year']])
df_exec["State_Year"] = df_exec["Year"].astype(str) + df_exec["MeetState"]
print(df_exec)
#df_exec['count'] = df_exec.groupby('meetid')['meetid'].transform('count')

#

#df_exec['State-Year'] = df_exec[['MeetState']]+df_exec[['Year']]
if grpst == 'True':
    if grpyr == 'True':
        df_exec['count'] = df_exec.groupby('State_Year')['State_Year'].transform('count')
        df_exec.drop_duplicates(subset="MeetState",
                        keep='first', inplace=True)
        df_exec.drop_duplicates(subset="State_Year",
                        keep='first', inplace=True)
        df1 =df_exec[['MeetState', 'MeetTown','Year','count','State_Year']]
    else:
        df_exec['count'] = df_exec.groupby('MeetState')['meetid'].transform('count')
        df_exec.drop_duplicates(subset="State_Year",
                        keep='first', inplace=True)
        df1 =df_exec[['MeetState', 'MeetTown','Year','count','State_Year']]
    #@pass
elif grpst == 'False':
    df_exec['count'] = df_exec.groupby('meetid')['meetid'].transform('count')
    df1 =df_exec[['MeetName', 'MeetState', 'MeetTown','Year','count','State_Year']]
    df1.drop_duplicates(subset="MeetName",
                     keep='first', inplace=True)

# if grpyr == 'True':
#     df_exec['count'] = df_exec.groupby('MeetState')['meetid'].transform('count')
#     df_exec.drop_duplicates(subset="MeetState",
#                      keep='first', inplace=True)
#     df1 =df_exec[['MeetState', 'MeetTown','Year','count']]
#     #@pass
# elif grpyr == 'False':
#     pass
#How many lifters, genders, weights, lifts, ----------------5/10


print(df1)
county = len(df1.index)
bleh = county
county = int(county) * 42
st.dataframe(df1,width=20000,height=county)

#Failed Lifts % Breakdown ---------------8/10 

#Number of lifters who went 9/9--------------------6/10

#BW Stats -------------------- 0/10
