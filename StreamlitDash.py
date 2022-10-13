from time import strptime
import pandas as pd 
import streamlit as st
from datetime import datetime

df = 'https://raw.githubusercontent.com/Ardmono/APU-Streamlit/main/filename.csv'
df = pd.read_csv(df)
df = df.drop(columns=['Age', 'Team', 'BirthYear', 'BirthDate','Country','State','Place','Equipment'])
df['Year'] = pd.DatetimeIndex(df['Date']).year
#Rename Best Bench/Deadlift/Squat
#Add Wilks Score
#Add Dots 
#print(df)
df = pd.DataFrame(df)
df_result_search = pd.DataFrame() 
st.set_page_config(layout="wide")



st.header(body='APU Australia 2018-2022')
st.text('Placeholder')
####Button Filters###
years = ['2018','2019','2020','2021','2022']
test = df['Date'].min
sex_input = st.sidebar.radio("Sex",options =("All","M","F"))
if sex_input == 'All':
    sex_input = df['Sex']
#####
#Need to filter weight class if gender is selected#
#####
weight_input = st.sidebar.multiselect("Weight Class",options=df['WeightClassKg'].unique())
if len(weight_input) == 0:
    weight_input = df['WeightClassKg']

  
#lift = st.sidebar.selectbox("Lift",options=('Any','Bench','Squat','Deadlift'))
Year = st.sidebar.multiselect("Year",options=years)
if len(Year) == 0:
    Year = df['Year']
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
#Liftername = st.sidebar.multiselect("Lifter Name",options=df['Name'].unique())
##weight_input = st.sidebar.selectbox("Weightclass",options=('All',df['WeightClassKg'].unique()))
#Filters = [sex_input, weight_input, Year, MeetState, MeetName, Liftername]

df_delection = df.query(
   "Sex==@sex_input & WeightClassKg==@weight_input & Year == @Year & MeetState == @meetState & MeetTown == @meetTown & MeetName == @meetName & Name == @liftername"
)

# df_delection = df.query(
#    "WeightClassKg==@weight_input &  Sex==@sexinputall | Sex==@sex_input "
# )


st.dataframe(df_delection,use_container_width=True,height=500)

task = ['Wilks Score', 'Dots', 'Year Fix', 'Style','Page','BestLift','Remove Floats']

st.header('To do')
for i in range(len(task)):
  st.checkbox(label=(task[i]))
  
