
import pandas as pd

import math
import streamlit as st

st.set_page_config(page_title='IPFGL Points Calculator',layout="wide",page_icon="🧊")
df = 'https://raw.githubusercontent.com/Ardmono/APU-Streamlit/main/filename.csv'
df = pd.read_csv(df)
df = df.drop(columns=['Age', 'Team', 'BirthYear', 'BirthDate','Country','State','Place','MeetCountry'])
df['Year'] = pd.DatetimeIndex(df['Date']).year
ipfglp = 0
selected_page = st.radio("Calculator Type: ", ["Simple", "Complicated"])
IPF_COEFFICIENTS1 = {
    'M': {
        'Raw': {
            'SBD': [1199.72839, 1025.18162, 0.009210],
            'B': [320.98041, 281.40258, 0.01008]
        },
        'Single-ply': {
            'SBD': [1236.25115, 1449.21864, 0.01644],
            'B': [381.22073, 733.79378, 0.02398]
        }
    },
    'F': {
        'Raw': {
            'SBD': [610.32796, 1045.59282, 0.03048],
            'B': [142.40398, 442.52671, 0.04724]
        },
        'Single-ply': {
            'SBD': [758.63878, 949.31382, 0.02435],
            'B': [221.82209, 357.00377, 0.02937]
        }
    }
}


#def goodlift(sex, equipment, event, bodyweight,total):
def ipf1(sex, equipment, event, bodyweightKg, totalKg):
    global IPF_COEFFICIENTS1

    # The IPF set lower bounds beyond which points are undefined.
    if bodyweightKg < 40 or totalKg <= 0:
        return 0

    # Normalize equipment to (Raw, Single-ply).
    if equipment == 'Wraps' or equipment == 'Straps':
        equipment = 'Raw'
    elif equipment == 'Multi-ply':
        equipment = 'Single-ply'

    # The IPF formula is only defined for some parameters.
    if equipment not in ['Raw', 'Single-ply']:
        return 0
    if event not in ['SBD', 'S', 'B', 'D']:
        return 0
    if sex not in ['M', 'F']:
        return 0    
    # Look up parameters.
    [a, b, c] = IPF_COEFFICIENTS1[sex][equipment][event]

    # Calculate the properties of the normal distribution.
    bwt = bodyweightKg
    p = totalKg
    e_pow = math.exp(-c * bwt)
    denominator = a - (b * e_pow)
    coeff = (a,b,c)
    #print(p*(100/denominator))
    return (p*(100/denominator))
   
if selected_page == 'Simple':
    col1, col2, col3,col5,col6 = st.columns(5,gap='Medium')
    with col1:
        bw = st.number_input('Bodyweight')
    with col2:
        tot = st.number_input('Total(KG)',step=0.25)
    with col3:
        sex = st.radio(label='Gender',options=('M','F'))
    with col5:
        equip = st.radio(label='Equipment',options=('Raw','Single-ply'))
    with col6:
        event = st.radio(label='Event',options=('SBD',  'B'))
    #with col4:
    #   result = st.button('Go')
    if tot > 1 and bw > 1:
            st.write('Your IPFGL Points are',round(ipf1(sex,equip,event,bw,tot),2))
            ipfglp = round(ipf1(sex,equip,event,bw,tot),2) 
            

    #if result:
        #st.write(ipf1(sex,equip,event,bw,totalkg))
elif selected_page == 'Complicated':
    col23, col32, col43,col34 = st.columns(4)
    with col23:
        bw = st.number_input('Bodyweight')
    with col32:
        sex = st.radio(label='Gender',options=('M','F'))
    with col43:
        equip = st.radio(label='Equipment',options=('Raw','Single-ply'))
    with col34:
        event = st.radio(label='Event',options=('SBD',  'B'))
    col11, col22, col33,col44 = st.columns(4,gap='Medium')
    with col11:
        sq = st.number_input('Squat', 0.00, 500.00,step=0.25)
    with col22:
        be = st.number_input('Bench', 0.00, 500.00,step=0.25)
    with col33:
        de = st.number_input('Deadlift', 0.00, 500.00,step=0.25)
    with col44:
        tot = sq+be+de
        if tot > 1:
            tot = float(tot)
            st.metric(label='Total',value=str(tot)+'Kg')
    if tot > 1 and bw > 1:
            st.write('Your IPFGL Points are',round(ipf1(sex,equip,event,bw,tot),2))
            ipfglp = round(ipf1(sex,equip,event,bw,tot),3) 
            #ipfglp = ipf1(sex,equip,event,bw,tot)
        

#df_delection = df
df_delection = df.query("Event == @event & Equipment == @equip")

st.text('IPFGL Points coeficient information can be found here - https://www.powerlifting.sport/fileadmin/ipf/data/ipf-formula/IPF_GL_Coefficients-2020.pdf')
df_delection = df_delection.reset_index(drop=True)
#df_delection = df_delection.sort_values(by = ['TotalKg'], ascending = [False])
df_delection = df_delection.sort_values(by = ['IPFGL'], ascending = [False])
df_delection = df_delection.reset_index(drop=True)
df_delection.index += 1 
ranker = int(df_delection.loc[df_delection['IPFGL'] <= ipfglp].index[0])

df_delection2 = df_delection[df_delection['Sex'] == sex]
df_delection2 = df_delection2.sort_values(by = ['IPFGL'], ascending = [False])
df_delection2 = df_delection2.reset_index(drop=True)
df_delection.index += 1 
ranker2 = int(df_delection2.loc[df_delection2['IPFGL'] <= ipfglp].index[0])

if sex == 'M':
    df_delection3 = df_delection[df_delection['Sex'] == sex]
    if bw > 66 and  bw < 74:
        wc = '74'
        df_delection3 = df_delection[df_delection['WeightClassKg'] == sex]

    #if df_delection[df_delection['WeightClassKg'] == sex]
if sex == 'F':
    df_delection3 = df_delection[df_delection['Sex'] == sex]
    if bw > 57 and  bw < 63:
        wc = '63'
        df_delection3 = df_delection[df_delection['WeightClassKg'] == sex]

    #if df_delection[df_delection['WeightClassKg'] == sex]
else:
    pass

df_delection3 = df_delection3.sort_values(by = ['IPFGL'], ascending = [False])
df_delection3 = df_delection3.reset_index(drop=True)
df_delection3.index += 1 
# else:
#     pass
# df_delection3 = df_delection[df_delection['WeightClassKg'] == sex]
# df_delection3 = df_delection3.sort_values(by = ['IPFGL'], ascending = [False])
# df_delection3 = df_delection3.reset_index(drop=True)
# df_delection.index += 1 
ranker3 = int(df_delection2.loc[df_delection2['IPFGL'] <= ipfglp].index[0])


aa = st.metric('Overall Placement: ',ranker)
bb = st.metric('Placement by Gender:',ranker2)
cc = st.metric('Placement by Weight Class: ', ranker3)
#cc = st.metric('Gender & Weightclass',1)
if 'bw' in globals():
    if 'tot' in globals(): 
        if bw > 1:
            if 'be' in globals(): 
                if tot > 1 and sq > 1 and be > 1 and de > 1:
                    ranker = int(df_delection.loc[df_delection['IPFGL'] < ipfglp].index[0])
                    aa, bb, cc = st.columns(3)
            else:
                if tot > 1:
                    aa, bb, cc = st.columns(3)
                    
                    
                
        