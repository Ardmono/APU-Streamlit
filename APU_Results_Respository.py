from select import select
from time import strptime
import pandas as pd 
import streamlit as st
from datetime import datetime
import time
import numpy as np


df = 'https://raw.githubusercontent.com/Ardmono/APU-Streamlit/main/filename.csv'
df = pd.read_csv(df)
df = df.drop(columns=['Age', 'Team', 'BirthYear', 'BirthDate','Country','State','Place','MeetCountry'])
df['Year'] = pd.DatetimeIndex(df['Date']).year
df.fillna(0, inplace=True)
listy = ['BodyweightKg' , 'Squat1Kg' , 'Squat2Kg'  ,'Squat3Kg' , 'Best3SquatKg',  'Bench1Kg',  'Bench2Kg' ,'Bench3Kg','Best3BenchKg',  'Deadlift1Kg',  'Deadlift2Kg', 'Deadlift3Kg' ,'Best3DeadliftKg'  ,'TotalKg']

df = pd.DataFrame(df)
df_result_search = pd.DataFrame() 
sst = time.time()

st.set_page_config(page_title="Main APU Database Page",layout="wide")



def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}



st.header(body='APU Australia -     ')
selected_page = st.radio("Show best lifts only: ", ["False", "True"])
####Button Filters###
years = ['2018','2019','2020','2021','2022']
test = df['Date'].min
img = 'https://raw.githubusercontent.com/Ardmono/APU-Streamlit/main/picture.jpg'
st.sidebar.image(img,width=300)   
#st.sidebar.text('Strength Club')   
#st.sidebar.header("Google.com")

###Keep this ####
# link = '[Join Strength Club](http://github.com)'
# st.sidebar.markdown(link, unsafe_allow_html=True)
# unsafe_allow_html=True
###Keep this ####

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
event = st.sidebar.multiselect("Lifter Event",options=df['Event'].unique())
if len(event) == 0:
    event = df['Event']
equpped = st.sidebar.radio("Equipment",options =("All","Raw","Single-ply"))
if equpped == 'All':
    equpped = df['Equipment']
fed = st.sidebar.radio("Sex",options =("APU","Other"))
if fed == 'Other':
    fed = df['Federation']

df_delection = df.query(
   "Sex==@sex_input & WeightClassKg==@weight_input & Year == @yer & MeetState == @meetState & MeetTown == @meetTown & MeetName == @meetName & Name == @liftername & Division == @divison & Event == @event & Equipment == @equpped & Federation == @fed"
)

if selected_page == 'True':
    df_delection = df_delection.drop(columns=['Squat1Kg', 'Squat2Kg' , 'Squat3Kg', 'Bench1Kg', 'Bench2Kg' , 'Bench3Kg', 'Deadlift1Kg','Deadlift2Kg','Deadlift3Kg','meetid'])
elif selected_page == 'False':
    pass

#df_delection = df_delection.reset_index(drop=True)
#df_delection = df_delection.sort_values(by = ['TotalKg'], ascending = [False])
df_delection = df_delection.reset_index(drop=True).sort_values(by = ['IPFGL'], ascending = [False])
df_delection = df_delection.reset_index(drop=True)
df_delection.index += 1 
#df_delection = df_delection.drop(columns=['index'])
#df = df_delection
st.dataframe(df_delection,use_container_width=True,height=1200)
print(df_delection)

   
et1 = time.time()
elapsed_time = et1 - sst

st.text(elapsed_time)

st.text(df.dtypes)


