import streamlit as st
import pandas as pd
st.title('Hello')
st.header("Header")
st.header("Dataframe Example")
data = pd.read_csv("details.xlsx",encoding='ISO-8859-1')
st.dataframe(data)