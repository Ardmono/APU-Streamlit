
import pandas as pd

import math
import streamlit as st
st.set_page_config(layout="wide")
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
   
col1, col2, col3,col5,col6,col4 = st.columns(6,gap='Medium')
with col1:
    bw = st.number_input('Bodyweight')
with col2:
    totalkg = st.number_input('Total(KG)')
with col3:
    sex = st.radio(label='Gender',options=('M','F'))
with col5:
    equip = st.radio(label='Equipment',options=('Raw','Single-ply'))
with col6:
    event = st.radio(label='Event',options=('SBD',  'B'))
with col4:
    result = st.button('Go')

if result:
    st.write(round(ipf1(sex,equip,event,bw,totalkg),2))

if result:
    st.write(ipf1(sex,equip,event,bw,totalkg))


st.markdown('##')
st.markdown('##')
st.header('Blank Space')
st.header('Blank Space1')
st.header('Blank Space2')
st.header('Blank Space3')
st.text('Lorem Ipsum')

sq, be, de,tot = st.columns(4,gap='Medium')
with sq:
    sq = st.slider('Squat', 0, 500)
with be:
    be = st.slider('Bench', 0, 500)
with de:
    de = st.slider('Deadlift', 0, 500)
with tot:
    tot = sq+be+de
    if tot > 1:
        tot = int(tot)
        st.metric(label='Total',value=tot)
    else 
    
if sq > 1 | be > 0:
    st.text('Test')

if sq > 0:
    total = sq+be+de
    st.write(total)


