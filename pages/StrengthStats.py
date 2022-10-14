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



lifts = df
lifts = lifts.dropna(axis=0)
lifts1 = lifts
len1 = len(lifts.index)
lifts = lifts.dropna(axis=0)

key = ['Squat1Kg', 'Squat2Kg', 'Squat3Kg', 'Bench1Kg', 'Bench2Kg', 'Bench3Kg', 'Deadlift1Kg', 'Deadlift2Kg', 'Deadlift3Kg']

lifts = lifts[lifts.columns & key]
#print(lifts)

test = lifts[lifts<0].count()

test1 = lifts.count()
countltl = df

#print(test)
lifts1['count'] = len1

test = test.sort_values(ascending=False)

#test2 = test.to_frame(name='test3')
test3 = pd.DataFrame({'lift':test.index, 'values':test.values})
test4 = pd.DataFrame({'lift':test.index, 'values':test.values.sum()})
test5 = test3 
#print(test4)
#test5 = test5.append(dict, ignore_index = True)
totaltest =  test5['values'].sum()
#print(totaltest)
test5.loc[len(test5.index)] = ['total', totaltest]


failedlifts = lifts
#failedlifts['fails'] = failedlifts.loc[failedlifts['Squat3Kg'] < 0]
#print(failedlifts)
#failedlifts['failb'] = failedlifts[failedlifts['Bench3Kg'] < 0 ]
# failedlifts['faild'] = failedlifts['Deadlift 3rd Attempt']<0
count = 0
def count_neg(x):
    global count
    if x < 0:
        count+=1
    else :
        count = 0 
    return count
#failedlifts['failb'] = failedlifts['Bench3Kg'].apply(count_neg)
#print(failedlifts)
testy = ['Squat3Kg', 'Bench3Kg']
for i in range(len(testy)):
  print(failedlifts[i])
  #print(failedlifts.columns[i])
# failedlifts['failsquat'] = failedlifts['Squat 3rd Attempt']
# #failedlifts.loc[failedlifts.failsquat > 0, 'failsquat'] = 0

# failedlifts['failbench'] = failedlifts['Bench 3rd Attempt']
# #failedlifts.loc[failedlifts.failbench > 0, 'failbench'] = 0

# failedlifts['faildead'] = failedlifts['Deadlift 3rd Attempt']
# #failedlifts.loc[failedlifts.faildead > 0, 'faildead'] = 0

# failedlifts['failsr'] = failedlifts['failsquat'].abs()
# failedlifts['failbr'] = failedlifts['failbench'].abs()
# failedlifts['faildr'] = failedlifts['faildead'].abs()   

# failedlifts['squatper'] =  round((failedlifts['failsr'] - failedlifts['Squat 2nd Attempt']) / failedlifts['Squat 1st Attempt'] * 100)
# failedlifts['benchper'] =  round((failedlifts['failbr'] - failedlifts['Bench 2nd Attempt']) / failedlifts['Bench 1st Attempt'] * 100)
# failedlifts['deadper'] =  round((failedlifts['faildr'] - failedlifts['Deadlift 2nd Attempt']) / failedlifts['Deadlift 1st Attempt'] * 100)