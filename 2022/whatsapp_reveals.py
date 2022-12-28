import streamlit as st
import pandas as pd

df = pd.read_csv('wa_santas_santees.csv')

st.title('🎅 Broke Bibliophiles Bangalore Secret Santa 2022 - Homenum Revelio !')
st.table(df)
