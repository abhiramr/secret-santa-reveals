import streamlit as st
import pandas as pd

df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTyECRVbMehaNx3Nqs7tFRQGSa1vR5UGe3uYLlNe_uzrd_Vs2HBMvhezx7sI2dftDGNhA-X_jwIYKSU/pub?gid=0&single=true&output=csv')

st.title('🎅 Broke Bibliophiles Bangalore Secret Santa 2022 - Homenum Revelio !')
st.table(df)
