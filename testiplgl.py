from re import X
import pandas as pd
import math
import streamlit as st
from points import ipf1


df = 'https://gitlab.com/openpowerlifting/opl-data/-/raw/main/meet-data/apu/2204/entries.csv'
df = pd.read_csv(df)
#df = df.drop(columns=['Age', 'Team', 'BirthYear', 'BirthDate','Country','State','Place','MeetCountry'])

def mult(x,y):
    x = x * y
    return x

#df['IPFGL'] = ipf1(df['Sex'],'Raw','SBD',70.2,440)
#df['pop2050'] = df.apply(lambda row: ipf1(row['population'],row['population_growth']),axis=1)
df['Bleh'] = df.apply(lambda row: ipf1(row['Sex'],row['Equipment'],row['Event'],row['BodyweightKg'],row['TotalKg']),axis=1)
#ipf1()
#df['Bleh'] = mult(x=df['TotalKg'])
df1 = df[['Name','Sex','TotalKg','Bleh']]
print(df1)
#df['IPFGL'] = ipf1(df['Sex'],)