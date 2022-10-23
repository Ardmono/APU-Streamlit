from select import select
from time import strptime
import pandas as pd 
import streamlit as st
from datetime import datetime
import time
import numpy as np
import openpyxl
import xlrd

gsheetid = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRiFVLT1NCUsXp3jnLJS9p4YC05rROZMntb2vqpZd-HQjUOhutBEzdsqjgijsQjSQ/pubhtml#"

d = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRiFVLT1NCUsXp3jnLJS9p4YC05rROZMntb2vqpZd-HQjUOhutBEzdsqjgijsQjSQ/pubhtml#/export?format=html&gid=0)&range=(A1NOTATION)'
#https://docs.google.com/spreadsheets/d/e/2PACX-1vRiFVLT1NCUsXp3jnLJS9p4YC05rROZMntb2vqpZd-HQjUOhutBEzdsqjgijsQjSQ/gviz/tq?tqx=out:csv&sheet=Data
#https://docs.google.com/spreadsheets/d/e/2PACX-1vRiFVLT1NCUsXp3jnLJS9p4YC05rROZMntb2vqpZd-HQjUOhutBEzdsqjgijsQjSQ/pubhtml#
df = pd.read_excel(gsheetid,engine='xlrd')