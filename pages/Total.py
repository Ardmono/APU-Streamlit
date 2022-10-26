
import pandas as pd

import math
import streamlit as st

sq, be, de,tot = st.columns(4,gap='Medium')
with col1:
    sq = st.slider('Squat', 0, 500)
with col2:
    be = st.slider('Bench', 0, 500)
with col3:
    de = st.slider('Deadlift', 0, 500)
with col4:
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
