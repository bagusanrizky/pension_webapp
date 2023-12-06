#import pandas as pd #pip install pandas openpyxl
import plotly.express as px # pip install plotly-express
import streamlit as st #pip install streamlit
#import matplotlib.pyplot as plt

st.set_page_config(page_title="PensionWebApp",
                   page_icon=":⏳:",
                   layout="wide"
)

st.title("Eksplorasi Data")
st.subheader("Distribusi Usia Pegawai")

fig_dist_usia = px.histogram(st.session_state.df, x="Usia sekarang (x)")
fig_dist_usia.update_layout(bargap=0.2, width=1000)
st.plotly_chart(fig_dist_usia)

st.subheader("Distribusi Gaji Per Unit Kerja")
fig_dist_gaji = px.histogram(st.session_state.df, 
                             x="Gaji Pokok", 
                             y="Unit Kerja UGM",
                             histfunc='avg'
)
fig_dist_gaji.update_xaxes(range=[1_500_000,3_500_000])
fig_dist_gaji.update_layout(width=1000, height=1000)
st.plotly_chart(fig_dist_gaji)
