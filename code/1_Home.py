import pandas as pd #pip install pandas openpyxl
#import plotly.express as px # pip install plotly-express
import streamlit as st #pip install streamlit
import openpyxl #pip install openpyxl

st.set_page_config(page_title="PensionWebApp",
                   page_icon=":⏳:",
                   layout="wide"
)

st.title("PensionWebApp")
st.subheader("Ini adalah draft WebApp untuk menghitung program pendanaan pensiun.")
st.sidebar.success("Pilih laman yang ingin Anda tuju.")

#check df key is in session state, initialize if not
if 'df' not in st.session_state:
    st.session_state.df = None

uploaded_file = st.file_uploader('Masukkan file excel (XLSX) yang ingin Anda analisis:', type='xlsx')
if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file, 
                       engine='openpyxl',
                       sheet_name='Peg tetap',
                       usecols='A:AK',
                       nrows=2668,
                       )
    st.session_state.df = df
    st.dataframe(df)
