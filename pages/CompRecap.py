from email.policy import default
from re import A
from time import strptime
import pandas as pd 
import streamlit as st
from datetime import datetime
import time
import numpy as np


df = 'https://raw.githubusercontent.com/Ardmono/APU-Streamlit/main/filename.csv'
df = pd.read_csv(df)
df = df.drop(columns=['Age', 'Team', 'BirthYear', 'BirthDate','Country','State','meetid','MeetCountry'])
df['Year'] = pd.DatetimeIndex(df['Date']).year
df.fillna(0, inplace=True)
df1 = df
#df1 = df1.drop(columns=['Age', 'Team', 'BirthYear', 'BirthDate','Country','State','Place','meetid','MeetCountry'])


df1 = df1[df1['Place'] != 'DQ']
listy = ['Squat1Kg' , 'Squat2Kg'  ,'Squat3Kg' ,  'Bench1Kg',  'Bench2Kg' ,'Bench3Kg',  'Deadlift1Kg',  'Deadlift2Kg', 'Deadlift3Kg']
for i in range(len(listy)):
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
 
df = df1
meetName = st.sidebar.multiselect("Meet Name",options=df['MeetName'].unique(),default=["National Classic Sub-Junior Junior and Master Powerlifting and Bench Press Championships"])

if len(meetName) == 0:
    meetName = df['MeetName']
sex_input = st.sidebar.radio("Sex",options =("All","M","F"))
if sex_input == 'All':
    sex_input = df['Sex']
eventy = st.sidebar.radio("Event",options=('SBD', 'B', 'BD', 'D','All'))
#if len(eventy) == 0:
#    eventy = 'SBD'
if eventy == 'All':
    eventy = df['Event']
st.header('Competition Recape, defaults to latest comp - ')
meeter = meetName
if len(meeter) == 0:
    meeter = 'All Comps'
st.text('Current Comp: '+str(meeter))
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
    
state = st.sidebar.multiselect("State",options=('NSW' ,'QLD' ,'WA', 'VIC' ,'ACT' , 'SA' ,'TAS'))
if len(state) == 0:
    state = df['MeetState']
print(df1.iloc[:,26:35])
df_exec = df.query(
   "Sex==@sex_input &  WeightClassKg==@weight_input & Equipment == @equpped & MeetState == @state & MeetName == @meetName & Event == @eventy"
)

#df_filtered = df_exec.query(len('Squat1Kg > 0 & Squat2Kg > 0 & Squat3Kg > 0'))
#['Squat1Kg' , 'Squat2Kg'  ,'Squat3Kg' ,  'Bench1Kg',  'Bench2Kg' ,'Bench3Kg',  'Deadlift1Kg',  'Deadlift2Kg', 'Deadlift3Kg']
#st.metric('All good squats', value=len(df_exec.query('Sex == 'F'')), delta=None, delta_color="normal", help=None)
dfsex = df.query(
   "WeightClassKg==@weight_input & Equipment == @equpped & MeetState == @state & MeetName == @meetName & Event == @eventy"
)


lifters = len(dfsex[dfsex['Sex'] =='F']) + len(dfsex[dfsex['Sex'] =='M'])
#print(lifters)
#print(df_exec[df_exec['Sex'] =='F'].count())
#st.metric('All good squats', value=len(df_exec.query('Sex == 'M'')), delta=None, delta_color="normal", help=None)
# st.metric(label="Count of failed Bench3",value=len(df_exec.query('Bench3Kgfail > 0')))
a, b,c = st.columns(3,gap='Medium')
a.metric(label="How Many Female Lifters", value=len(dfsex[df['Sex'] =='F']))
b.metric(label="How Many Male Lifters", value=len(dfsex[df['Sex'] =='M']))
c.metric(label="How Many Total Lifters", value=lifters)
#d.metric(label="Total KG of all lifted weights", value=(str(df_exec['TotalKg'].sum())+' Kg'))

col1, col2, col3,col4,col5 = st.columns(5,gap='Medium')
col1.metric(label="How Many Lifters", value=len(df_exec.query('Bench3Kgfail > 0')))
col2.metric(label="Gender Ratios", value=len(df_exec.query('Bench3Kgfail < 1')))
col3.metric(label="% Succesful Lifts", value=len(df_exec.query('Bench3Kgfail > -1')))
col4.metric(label="Total KG of all lifted weights", value=(str(df_exec['TotalKg'].sum())+' Kg'))
col5.metric(label="Count of 9/9 Lifts",value=len(df_exec.query('Squat3Kg > 1 & Squat2Kg > 1 & Squat1Kg > 1 & Bench1Kg > 1 & Bench2Kg > 1 & Bench3Kg > 1 & Deadlift1Kg > 1 & Deadlift2Kg > 1 & Deadlift3Kg > 1')))

totalweight = df_exec['TotalKg'].sum()
print(totalweight)
data = [0,0,0]
fails = pd.DataFrame(columns=['Squat1','Squat2','Squat3','Bench1','Bench2','Bench3','Deadlift1','Deadlift2','Deadlift3'],index=['Succeed','Fail','Attempted','Percentage'])
#fails = fails[['Succeed','Fail','Attempted']]
print(fails)
list1 = ['Squat1','Squat2','Squat3','Bench1','Bench2','Bench3','Deadlift1','Deadlift2','Deadlift3']
list2 = ['Squat1Kgfail' , 'Squat2Kgfail'  'Squat3Kgfail'  'Bench1Kgfail'  'Bench2Kgfail'  'Bench3Kgfail'  'Deadlift1Kgfail'  'Deadlift2Kgfail'  'Deadlift3Kgfail']



##Squats
fails['Squat1'][0] = len(df_exec.query('Squat1Kgfail < 1'))
fails['Squat1'][1] = len(df_exec.query('Squat1Kgfail > 0'))
fails['Squat1'][2] = len(df_exec.query('Squat1Kgfail > -1'))
fails['Squat1'][3] = fails['Squat1'][0] / fails['Squat1'][2] * 100

fails['Squat2'][0] = len(df_exec.query('Squat2Kgfail < 1'))
fails['Squat2'][1] = len(df_exec.query('Squat2Kgfail > 0'))
fails['Squat2'][2] = len(df_exec.query('Squat2Kgfail > -1'))
fails['Squat2'][3] = fails['Squat2'][0] / fails['Squat2'][2] * 100

fails['Squat3'][0] = len(df_exec.query('Squat3Kgfail < 1'))
fails['Squat3'][1] = len(df_exec.query('Squat3Kgfail > 0'))
fails['Squat3'][2] = len(df_exec.query('Squat3Kgfail > -1'))
fails['Squat3'][3] = fails['Squat3'][0] / fails['Squat3'][2] * 100
##Squats

#Bench
fails['Bench1'][0] = len(df_exec.query('Bench1Kgfail < 1'))
fails['Bench1'][1] = len(df_exec.query('Bench1Kgfail > 0'))
fails['Bench1'][2] = len(df_exec.query('Bench1Kgfail > -1'))
fails['Bench1'][3] = fails['Bench1'][0] / fails['Bench1'][2] * 100

fails['Bench2'][0] = len(df_exec.query('Bench2Kgfail < 1'))
fails['Bench2'][1] = len(df_exec.query('Bench2Kgfail > 0'))
fails['Bench2'][2] = len(df_exec.query('Bench2Kgfail > -1'))
fails['Bench2'][3] = fails['Bench2'][0] / fails['Bench2'][2] * 100

fails['Bench3'][0] = len(df_exec.query('Bench3Kgfail < 1'))
fails['Bench3'][1] = len(df_exec.query('Bench3Kgfail > 0'))
fails['Bench3'][2] = len(df_exec.query('Bench3Kgfail > -1'))
fails['Bench3'][3] = fails['Bench3'][0] / fails['Bench3'][2] * 100
#Bench

#Deadlift
fails['Deadlift1'][0] = len(df_exec.query('Deadlift1Kgfail < 1'))
fails['Deadlift1'][1] = len(df_exec.query('Deadlift1Kgfail > 0'))
fails['Deadlift1'][2] = len(df_exec.query('Deadlift1Kgfail > -1'))
fails['Deadlift1'][3] = fails['Deadlift1'][0] / fails['Deadlift1'][2] * 100
fails['Deadlift1'][3] = float(fails['Deadlift1'][3])

fails['Deadlift2'][0] = len(df_exec.query('Deadlift2Kgfail < 1'))
fails['Deadlift2'][1] = len(df_exec.query('Deadlift2Kgfail > 0'))
fails['Deadlift2'][2] = len(df_exec.query('Deadlift2Kgfail > -1'))
fails['Deadlift2'][3] = fails['Deadlift2'][0] / fails['Deadlift2'][2] * 100

fails['Deadlift3'][0] = len(df_exec.query('Deadlift3Kgfail < 1'))
fails['Deadlift3'][1] = len(df_exec.query('Deadlift3Kgfail > 0'))
fails['Deadlift3'][2] = len(df_exec.query('Deadlift3Kgfail > -1'))
fails['Deadlift3'][3] = fails['Deadlift3'][0] / fails['Deadlift3'][2] * 100
#Deadlift


print(fails)

st.dataframe(fails,use_container_width=True)
#st.dataframe(df_exec,use_container_width=True,height=1200)

# task = df1['WeightClassKg'].unique()

# rslt_df = df1.loc[df1['WeightClassKg'] == 57]
# col4, col1, col2,col3 = st.columns(4)
# col4.metric("Weight Class",task[i])
# col1.metric("Bench", (rslt_df[rslt_df['Bench3Kgfail' > 0]].count()))
# col2.metric("Deadlift", (rslt_df['Deadlift3Kgfail'].count()))
# col3.metric('Squat',(rslt_df['Squat3Kgfail'].count()))
# # result = []



# task = df1['WeightClassKg'].unique()
# #print(task)
# for i in range(len(task)):
#     #print(task[i])
#     rslt_df = df1.loc[df1['WeightClassKg'] == task[i]]
#     #print(rslt_df)
#     col4, col1, col2,col3 = st.columns(4)
#     col4.metric("Weight Class",task[i])
#     col1.metric("Bench", (rslt_df['Bench3Kgfail'].count()))
#     col2.metric("Deadlift", (rslt_df['Deadlift3Kgfail'].count()))
#     col3.metric('Squat',(rslt_df['Squat3Kgfail'].count()))
    
    

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
