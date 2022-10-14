from time import strptime
import pandas as pd 
import streamlit as st
from datetime import datetime
import time
import numpy as np

df = 'https://raw.githubusercontent.com/Ardmono/APU-Streamlit/main/filename.csv'
df = pd.read_csv(df)
df = df.drop(columns=['Age', 'Team', 'BirthYear', 'BirthDate','Country','State','Place','Equipment','meetid','MeetCountry'])
df['Year'] = pd.DatetimeIndex(df['Date']).year
df.fillna(0, inplace=True)
listy = ['BodyweightKg' , 'Squat1Kg' , 'Squat2Kg'  ,'Squat3Kg' , 'Best3SquatKg',  'Bench1Kg',  'Bench2Kg' ,'Bench3Kg','Best3BenchKg',  'Deadlift1Kg',  'Deadlift2Kg', 'Deadlift3Kg' ,'Best3DeadliftKg'  ,'TotalKg']
for i in range(len(listy)):
  df[listy[i]] = df[listy[i]].astype(np.float32)
df['BodyweightKg'] = df['BodyweightKg'].astype(np.float16)
df.round({'BodyweightKg': 2})
img = 'https://scontent-syd2-1.xx.fbcdn.net/v/t39.30808-6/305564434_2408090155999032_1724872612072231495_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=a26aad&_nc_ohc=JmGtrTla1M4AX_e2BTD&_nc_ht=scontent-syd2-1.xx&oh=00_AT98tkicuZfegT379kCrYFvZ-BNyJ8z8CJUrhljx6dZUDA&oe=634D6D7C'

df = pd.DataFrame(df)
df_result_search = pd.DataFrame() 
sst = time.time()

st.set_page_config(layout="wide")



#st.header(body='APU Australia')
#st.image(img,width=150)
#st.text('Placeholder 1 ')

st.markdown('''
# Sections
- [Section 1](#section-1)
- [Section 2](#apu-australia)
''', unsafe_allow_html=True)
st.header('')
#st.image(img,width=2000)
st.header(body='APU Australia')
####Button Filters###
years = ['2018','2019','2020','2021','2022']
test = df['Date'].min
st.sidebar.image(img,width=200)   
#st.sidebar.text('Strength Club')   
#st.sidebar.header("Google.com")
link = '[Join Strength Club](http://github.com)'
st.sidebar.markdown(link, unsafe_allow_html=True)
unsafe_allow_html=True
sex_input = st.sidebar.radio("Sex",options =("All","M","F"))
if sex_input == 'All':
    sex_input = df['Sex']
weight_input = st.sidebar.multiselect("Weight Class",options=df['WeightClassKg'].unique())
if len(weight_input) == 0:
    weight_input = df['WeightClassKg']
yer = st.sidebar.multiselect("Year",options=df['Year'].unique())
if len(yer) == 0:
    yer = df['Year']
meetState = st.sidebar.multiselect("Meet State",options=('NSW' ,'QLD' ,'WA', 'VIC' ,'ACT' , 'SA' ,'TAS'))
if len(meetState) == 0:
    meetState = df['MeetState']
meetTown = st.sidebar.multiselect("Meet Town",options=df['MeetTown'].unique())
if len(meetTown) == 0:
    meetTown = df['MeetTown']
meetName = st.sidebar.multiselect("Meet Name",options=df['MeetName'].unique())
if len(meetName) == 0:
    meetName = df['MeetName']
liftername = st.sidebar.multiselect("Lifter Name",options=df['Name'].unique())
if len(liftername) == 0:
    liftername = df['Name']
divison = st.sidebar.multiselect("Lifter Division",options=df['Division'].unique())
if len(divison) == 0:
    divison = df['Division']

df_delection = df.query(
   "Sex==@sex_input & WeightClassKg==@weight_input & Year == @yer & MeetState == @meetState & MeetTown == @meetTown & MeetName == @meetName & Name == @liftername & Division == @divison"
)


st.dataframe(df_delection,use_container_width=True,height=1200)

task = ['Wilks Score', 'Dots', 'Year Fix', 'Style','Page','BestLift']

st.header('To do')
for i in range(len(task)):
  st.checkbox(label=(task[i]))
if st.checkbox(label='Remove Floats'):
    value=True
   
et1 = time.time()
elapsed_time = et1 - sst

st.text(elapsed_time)

st.text(df.dtypes)

