
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
    bleh = sex_input
    sex_input = df['Sex']
else:
    bleh = sex_input
    
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
    
state = st.sidebar.multiselect("State",options=('NSW' ,'QLD' ,'WA', 'VIC' ,'ACT' , 'SA' ,'TAS'))
if len(state) == 0:
    state = df['MeetState']
#print(df1.iloc[:,26:35])
df_exec = df.query(
   "Sex==@sex_input &  WeightClassKg==@weight_input & Equipment == @equpped & MeetState == @state & MeetName == @meetName & Event == @eventy"
)

#df_filtered = df_exec.query(len('Squat1Kg > 0 & Squat2Kg > 0 & Squat3Kg > 0'))
#['Squat1Kg' , 'Squat2Kg'  ,'Squat3Kg' ,  'Bench1Kg',  'Bench2Kg' ,'Bench3Kg',  'Deadlift1Kg',  'Deadlift2Kg', 'Deadlift3Kg']
#st.metric('All good squats', value=len(df_exec.query('Sex == 'F'')), delta=None, delta_color="normal", help=None)
dfsex = df.query(
   "WeightClassKg==@weight_input & Equipment == @equpped & MeetState == @state & MeetName == @meetName & Event == @eventy"
)

blut = 'String'
lifters = len(dfsex[dfsex['Sex'] =='F']) + len(dfsex[dfsex['Sex'] =='M'])
#print(lifters)
#print(df_exec[df_exec['Sex'] =='F'].count())
#st.metric('All good squats', value=len(df_exec.query('Sex == 'M'')), delta=None, delta_color="normal", help=None)
# st.metric(label="Count of failed Bench3",value=len(df_exec.query('Bench3Kgfail > 0')))
a, b,c = st.columns(3,gap='Small')
a.metric(label="Female Lifters", value=len(dfsex[df['Sex'] =='F']))
b.metric(label="Male Lifters", value=len(dfsex[df['Sex'] =='M']))
c.metric(label="Total Lifters", value=lifters)
#d.metric(label="Total KG of all lifted weights", value=(str(df_exec['TotalKg'].sum())+' Kg'))
st.text('Current Comp: '+str(meeter))
col1, col2, col3,col4,col5,col33 = st.columns(6,gap='Medium')
col1.metric(label="How Many Lifters", value=len(df_exec.query('Bench3Kgfail > 0')))
col2.metric(label="Gender Ratios", value='Bleh')
col3.metric(label="% Succesful Lifts", value='Bleh')
col33.metric(label="Most failed lift", value=blut)
col4.metric(label="Total KG of all lifted weights", value=(str(df_exec['TotalKg'].sum())+' Kg'))
col5.metric(label="Count of 9/9 Lifts",value=len(df_exec.query('Squat3Kg > 1 & Squat2Kg > 1 & Squat1Kg > 1 & Bench1Kg > 1 & Bench2Kg > 1 & Bench3Kg > 1 & Deadlift1Kg > 1 & Deadlift2Kg > 1 & Deadlift3Kg > 1')))

totalweight = df_exec['TotalKg'].sum()
#print(totalweight)
data = [0,0,0]


    

fails = pd.DataFrame(columns=['Lift','Succeed','Fail','Attempted','Percentage'])

lifts = ['Squat1','Squat2','Squat3','Bench1','Bench2','Bench3','Deadlift1','Deadlift2','Deadlift3']
#fails = fails[['Succeed','Fail','Attempted']]

list1 = ['Squat1','Squat2','Squat3','Bench1','Bench2','Bench 3rd','Deadlift1','Deadlift2','Deadlift3']
list2 = ['Squat1Kgfail' , 'Squat2Kgfail'  'Squat3Kgfail'  'Bench1Kgfail'  'Bench2Kgfail'  'Bench3Kgfail'  'Deadlift1Kgfail'  'Deadlift2Kgfail'  'Deadlift3Kgfail']



##Squats
#fails.at[1,'Succeed']= len(df_exec.query('Squat1Kgfail < 1'))
fails.loc[0,['Lift','Succeed','Fail','Attempted','Percentage']] =  ['Squat1',(len(df_exec.query('Squat1Kgfail < 1'))),(len(df_exec.query('Squat1Kgfail > 0'))),(len(df_exec.query('Squat1Kgfail > -1'))),(len(df_exec.query('Squat1Kgfail < 1'))) / (len(df_exec.query('Squat1Kgfail > -1'))) * 100]

fails.loc[1,['Lift','Succeed','Fail','Attempted','Percentage']] = ['Squat2',(len(df_exec.query('Squat2Kgfail < 1'))),(len(df_exec.query('Squat2Kgfail > 0'))),(len(df_exec.query('Squat2Kgfail > -1'))),(len(df_exec.query('Squat2Kgfail < 1'))) / (len(df_exec.query('Squat2Kgfail > -1'))) * 100]
fails.loc[2,['Lift','Succeed','Fail','Attempted','Percentage']] = ['Squat3',(len(df_exec.query('Squat3Kgfail < 1'))),(len(df_exec.query('Squat3Kgfail > 0'))),(len(df_exec.query('Squat3Kgfail > -1'))),(len(df_exec.query('Squat3Kgfail < 1'))) / (len(df_exec.query('Squat3Kgfail > -1'))) * 100]

fails.loc[3,['Lift','Succeed','Fail','Attempted','Percentage']] = ['Bench1',(len(df_exec.query('Bench1Kgfail < 1'))),(len(df_exec.query('Bench1Kgfail > 0'))),(len(df_exec.query('Bench1Kgfail > -1'))),(len(df_exec.query('Bench1Kgfail < 1'))) / (len(df_exec.query('Bench1Kgfail > -1'))) * 100]
fails.loc[4,['Lift','Succeed','Fail','Attempted','Percentage']] = ['Bench2',(len(df_exec.query('Bench2Kgfail < 1'))),(len(df_exec.query('Bench2Kgfail > 0'))),(len(df_exec.query('Bench2Kgfail > -1'))),(len(df_exec.query('Bench2Kgfail < 1'))) / (len(df_exec.query('Bench2Kgfail > -1'))) * 100]
fails.loc[5,['Lift','Succeed','Fail','Attempted','Percentage']] = ['Bench3',(len(df_exec.query('Bench3Kgfail < 1'))),(len(df_exec.query('Bench3Kgfail > 0'))),(len(df_exec.query('Bench3Kgfail > -1'))),(len(df_exec.query('Bench3Kgfail < 1'))) / (len(df_exec.query('Bench3Kgfail > -1'))) * 100]

fails.loc[6,['Lift','Succeed','Fail','Attempted','Percentage']] = ['Deadlift1',(len(df_exec.query('Deadlift1Kgfail < 1'))),(len(df_exec.query('Deadlift1Kgfail > 0'))),(len(df_exec.query('Deadlift1Kgfail > -1'))),(len(df_exec.query('Deadlift1Kgfail < 1'))) / (len(df_exec.query('Deadlift1Kgfail > -1'))) * 100]
fails.loc[7,['Lift','Succeed','Fail','Attempted','Percentage']] = ['Deadlift2',(len(df_exec.query('Deadlift2Kgfail < 1'))),(len(df_exec.query('Deadlift2Kgfail > 0'))),(len(df_exec.query('Deadlift2Kgfail > -1'))),(len(df_exec.query('Deadlift2Kgfail < 1'))) / (len(df_exec.query('Deadlift2Kgfail > -1'))) * 100]
fails.loc[8,['Lift','Succeed','Fail','Attempted','Percentage']] = ['Deadlift3',(len(df_exec.query('Deadlift3Kgfail < 1'))),(len(df_exec.query('Deadlift3Kgfail > 0'))),(len(df_exec.query('Deadlift3Kgfail > -1'))),(len(df_exec.query('Deadlift3Kgfail < 1'))) / (len(df_exec.query('Deadlift3Kgfail > -1'))) * 100]

#testyi = fails['Percentage']=fails.idxmin(axis=1)
testyi = fails[fails.Percentage == fails.Percentage.min()]
print(testyi)
st.text(testyi)
#fails['Squat1'][3] = fails['Squat1'][0] / fails['Squat1'][2] * 100

#ails.loc[0,['Percentage']] = 0 
#print((len(df_exec.query('Squat1Kgfail < 1'))) / (len(df_exec.query('Squat1Kgfail > -1'))) * 100)
fig = go.Figure(data=[
    go.Bar(name='Succeed', x=fails.Lift, y=fails.Succeed),
    go.Bar(name='Fail', x=fails.Lift, y=fails.Fail),
    #go.Bar(name='Attempted', x=fails.Lift, y=fails.Attempted,),
    
])
## Need to add labels 

lengthy = len(df_exec.query('Deadlift3Kgfail > -1'))
fig.update_layout(barmode='stack')
fig.update_layout(yaxis_range=[0,lengthy])

#fig.show()

df_delection = df_exec.reset_index(drop=True).sort_values(by = ['IPFGL'], ascending = [False])
df_delection = df_delection.reset_index(drop=True)
df_delection.index += 1 
df_delection = df_delection.head(10)
#df_delection = df_delection.drop(columns=['Squat1Kgfail' , 'Squat2Kgfail'  'Squat3Kgfail'  'Bench1Kgfail'  'Bench2Kgfail'  'Bench3Kgfail'  'Deadlift1Kgfail'  'Deadlift2Kgfail'  'Deadlift3Kgfail'])

county = 10 * 42
county = int(county)
# if bleh == 'All':
#     st.dataframe(df_delection,use_container_width=True,height=county)
if bleh == 'M':
        st.dataframe(df_delection,use_container_width=True,height=county)
elif bleh == 'F':
        st.dataframe(df_delection,use_container_width=True,height=county)
else:
    dfm = df_delection
    dff = df_delection
    st.header('Female')
    st.dataframe(dff,use_container_width=True,height=county)
    st.header('Male')
    st.dataframe(dfm,use_container_width=True,height=county)


st.plotly_chart(fig, use_container_width=True)
#print(fails)

st.dataframe(fails,use_container_width=True)

st.text('Need to add IPFGL Point Calculation/Scoring')

#How many lifters, genders, weights, lifts, ----------------5/10

#Failed Lifts % Breakdown ---------------8/10 

#Number of lifters who went 9/9--------------------6/10

#BW Stats -------------------- 0/10
