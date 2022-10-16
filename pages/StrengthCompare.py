from time import strptime
import pandas as pd 
import streamlit as st
from datetime import datetime
import time
import numpy as np


df = 'https://raw.githubusercontent.com/Ardmono/APU-Streamlit/main/filename.csv'
df = pd.read_csv(df)
df = df.drop(columns=['Age', 'Team', 'BirthYear', 'BirthDate','Country','State','Place','meetid','MeetCountry'])
df['Year'] = pd.DatetimeIndex(df['Date']).year
df.fillna(0, inplace=True)



#st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
#st.metric('Best Bench', value, delta=None, delta_color="normal", help=None)

#bodyweight = st.number_input("Bodyweight")
col1, col2, col3 = st.columns(3)



bodyweight = st.number_input("Bodyweight")
benchtotal = st.select_slider("Sex", options=['Male', 'Female'])
benchtotal = st.number_input("Bench Best")
deadlift = st.number_input("Deadlift Best")
squat = st.number_input("Squat Best")
if len(bodyweight) == 0:
    bodyweight = 'Enter bodyweight'
col1.metric(bodyweight, "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
#bodyweight = st.number_input("Bodyweight")
#if len(benchtotal) == 0:
#    benchtotal = df['MeetState']


# def main_page():
#     #st.markdown("# Main page 🎈")
#     st.sidebar.markdown("# Main page 🎈")

# def page2():
#     #st.markdown("# Page 2 ❄️")
#     st.sidebar.markdown("# Page 2 ❄️")

# def page3():
#     #st.markdown("# Page 3 🎉")
#     st.sidebar.markdown("# Page 3 🎉")

# page_names_to_funcs = {
#     "Main Page": main_page,
#     "Page 2": page2,
#     "Page 3": page3,
# }

# selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
# page_names_to_funcs[selected_page]()
