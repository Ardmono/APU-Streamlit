import pandas as pd 
import streamlit as st
from datetime import datetime
import time
import numpy as np
import plotly.graph_objects as go

csv = 'C:\\Users\\Callum\\Documents\\Python\\APU-Streamlit\\filename.csv'

df = pd.read_csv(csv)

df.loc[df["meetid"] == 1808, "MeetTown"] = 'Yatala'

df.to_csv('C:\\Users\\Callum\\Documents\\Python\\APU-Streamlit\\filename.csv',index=False)