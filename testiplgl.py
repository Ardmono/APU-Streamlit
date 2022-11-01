from operator import index
from re import X
import re
import pandas as pd
import math
import streamlit as st
from points import ipf1


# df = 'https://gitlab.com/openpowerlifting/opl-data/-/raw/main/meet-data/apu/2204/entries.csv'
# df = pd.read_csv(df)
# #df = df.drop(columns=['Age', 'Team', 'BirthYear', 'BirthDate','Country','State','Place','MeetCountry'])

# def mult(x,y):
#     x = x * y
#     return x

# #df['IPFGL'] = ipf1(df['Sex'],'Raw','SBD',70.2,440)
# #df['pop2050'] = df.apply(lambda row: ipf1(row['population'],row['population_growth']),axis=1)
# #df['Bleh'] = df.apply(lambda row: ipf1(row['Sex'],row['Equipment'],row['Event'],row['BodyweightKg'],row['TotalKg']),axis=1)
# #ipf1()
# #df['Bleh'] = mult(x=df['TotalKg'])
# df1 = df[['Name','Sex','TotalKg','Bleh']]
#print(df1)
#df['IPFGL'] = ipf1(df['Sex'],)

listy = [6, 7, 3, 8, 19, 34, 50, 2]
df = pd.DataFrame(listy, columns=['Numbers'])
listy = sorted(listy,reverse=True)

#print(df)
df_delection = df.reset_index(drop=True)
#df_delection = df_delection.sort_values(by = ['TotalKg'], ascending = [False])
df_delection = df_delection.sort_values(by = ['Numbers'], ascending = [False])
df_delection = df_delection.reset_index(drop=True)
df_delection.index += 1 
b = 9
val = 0
#print(df_delection)
# def findrank():
#     for i in df_delection['Numbers']:
#         if b > i:
#             val = i
#             print(i)
#             break
#         else:
#             pass
# findrank()        
# print(val)
#print(df_delection)
print(df_delection.loc[df_delection['Numbers'] < 8].index[0])