import pandas as pd 
import streamlit as st
from datetime import datetime
import time
import numpy as np
import plotly.graph_objects as go

csv = 'C:\\Users\\Callum\\Documents\\Python\\APU-Streamlit\\filename.csv'

df = pd.read_csv(csv)


df.loc[df["meetid"] == 1808, "MeetTown"] = 'Yatala'
df.loc[df["meetid"] == 1813, "MeetTown"] = 'Campbelltown'
df.loc[df["meetid"] == 1818, "MeetTown"] = 'UNK'
df.loc[df["meetid"] == 2011, "MeetTown"] = 'UNK'
df.loc[df["meetid"] == 2012, "MeetTown"] = 'UNK'
df.loc[df["meetid"] == 2020, "MeetTown"] = 'UNK'
df.loc[df["meetid"] == 2016, "MeetTown"] = 'UNK'
df.loc[df["meetid"] == 2103, "MeetTown"] = 'UNK'
df.loc[df["meetid"] == 2105, "MeetTown"] = 'UNK'
df.loc[df["meetid"] == 2106, "MeetTown"] = 'UNK'
df.loc[df["meetid"] == 2119, "MeetTown"] = 'UNK'
df.loc[df["meetid"] == 2121, "MeetTown"] = 'UNK'
df.loc[df["meetid"] == 2122, "MeetTown"] = 'UNK'
df.loc[df["meetid"] == 2226, "MeetTown"] = 'UNK'
df.loc[df["meetid"] == 2228, "MeetTown"] = 'UNK'
df.loc[df["meetid"] == 2234, "MeetTown"] = 'UNK'

df.loc[df["meetid"] == 2122, "MeetState"] = 'UNK'
df.loc[df["meetid"] == 2130, "MeetState"] = 'UNK'
df.loc[df["meetid"] == 2020, "MeetState"] = 'UNK'
df.loc[df["meetid"] == 2019, "MeetState"] = 'UNK'

df.loc[df["meetid"] == 2130, "MeetTown"] = 'Collate'
df.loc[df["meetid"] == 2130, "MeetState"] = 'Collate'

df.to_csv('C:\\Users\\Callum\\Documents\\Python\\APU-Streamlit\\filename.csv',index=False)