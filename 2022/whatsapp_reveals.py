import streamlit as st
import pandas as pd

df = pd.read_csv('wa_santas_santees.csv')

st.title('Santa and Santee List')
st.table(df)
