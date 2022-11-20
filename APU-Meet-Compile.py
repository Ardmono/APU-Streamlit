from operator import index
from colorama import Cursor
import pandas as pd
import time

st = time.time()
meetid1 = 1801
url5 = 'https://gitlab.com/openpowerlifting/opl-data/-/raw/main/meet-data/apu/1801/entries.csv'
df1 = pd.read_csv(url5)
url6 = 'https://gitlab.com/openpowerlifting/opl-data/-/raw/main/meet-data/apu/1801/meet.csv'
df2 = pd.read_csv(url6)

df1 = df1.assign(meetid=meetid1)
df2 = df2.assign(meetid=meetid1)

#print(df1,df2)

df1 =pd.merge(df1,df2,on='meetid',how='left')
# print(df3)


start = 1802
num = 1
complist = []
# for i in range(3):
#     #global num
#     url = "https://gitlab.com/openpowerlifting/opl-data/-/raw/main/meet-data/apu/"+str(start)+"/meet.csv".format(i)
#     start += 1
#     complist.append(url)
# #print(complist)

for i in range(500):
        try:
            url = "https://gitlab.com/openpowerlifting/opl-data/-/raw/main/meet-data/apu/"+str(start)+"/entries.csv"
            url2 = "https://gitlab.com/openpowerlifting/opl-data/-/raw/main/meet-data/apu/"+str(start)+"/meet.csv"
            #print(start)
            url = pd.read_csv(url,header=0)
            url2 = pd.read_csv(url2,header=0)
            url = url.assign(meetid=start)
            url2 = url2.assign(meetid=start)  
            urlcomb =pd.merge(url,url2,on='meetid',how='left')      
            #url.drop(columns=['Equipment'])
            #print(url)
            df1 = pd.concat([df1, urlcomb])
            #complist.append(url)
            et = time.time()
            elapsed_time = et - st
            print('Added APU '+str(start)+' to CSV - Execution time:', elapsed_time, 'seconds')
            start += 1
            
        except:
            elapsed_time = et - st
            print('APU '+str(start)+' does not exist CSV -  Execution time:', elapsed_time, 'seconds')
            start += 1
#print(df1)
df1.to_csv('filename.csv',index=False)
print(df1)

et1 = time.time()
elapsed_time = et1 - st
print('Execution time:', elapsed_time, 'seconds')

start = 1802
def apu_compile_csv():
    global start
    for i in range(3):  
        try:
            url1 = "https://gitlab.com/openpowerlifting/opl-data/-/raw/main/meet-data/apu/"+str(start)+"/meet.csv"
            #print(url1)
            ##print(start)
            lift_url = pd.read_csv(url1)
            start += 1
            #print(lift_url)
            pd.concat([df1, lift_url], ignore_index=True)
            #print("Success - APU No. "+str(start)+" Does exist")
        except Exception:
            pass
            #print("Error - APU No. "+str(start)+" Does not exist")
            start += 1

#apu_compile_csv()
#print(df1)
et1 = time.time()
elapsed_time = et1 - st
print('Execution time:', elapsed_time, 'seconds')