import pandas as pd #pip install pandas openpyxl
import plotly.express as px # pip install plotly-express
import streamlit as st #pip install streamlit
import streamlit.components.v1 as components
#import matplotlib.pyplot as plt

st.set_page_config(page_title="PensionWebApp",
                   page_icon=":⏳:",
                   layout="wide"
)

st.title("Input Assumption")

# --- INPUT ANGKA ---

# Create or load your DataFrame
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()

# Define your initial input values
tingkat_bunga = st.number_input("Tingkat bunga aktuaria (per tahun)", min_value=0.000, max_value=1.000, format="%f")
tingkat_kenaikan_gaji = st.number_input("Tingkat kenaikan gaji (per tahun)", min_value=0.000, max_value=1.000, format="%f")
replacement_ratio_max = 0.75
replacement_ratio_min = 0.4
pensiun_normal_ratio = 0.025

# Function to recalculate variables
def recalculate_variables():
    st.session_state.df["Gapok Terakhir"] = st.session_state.df["Gaji Pokok"] * (1 + tingkat_kenaikan_gaji) ** (st.session_state.df["Usia Pensiun (r) "] - st.session_state.df["Usia sekarang (x)"] - 1)
    st.session_state.df["Benefit Pensiun Normal (1 Bulan)"] = 0.025 * st.session_state.df["Total Masa Kerja Harapan (MK)"] * st.session_state.df["Gapok Terakhir"]

    condition_1 = st.session_state.df["Total Masa Kerja Harapan (MK)"] >= 20
    condition_2 = st.session_state.df["Total Masa Kerja Harapan (MK)"] > replacement_ratio_max / pensiun_normal_ratio
    condition_3 = st.session_state.df["Total Masa Kerja Harapan (MK)"] < replacement_ratio_min / pensiun_normal_ratio

    st.session_state.df.loc[condition_1 & condition_2, "Benefit Pensiun Normal Taspen (1 Bulan)"] = replacement_ratio_max * st.session_state.df.loc[condition_1 & condition_2, "Gapok Terakhir"]
    st.session_state.df.loc[condition_1 & condition_3, "Benefit Pensiun Normal Taspen (1 Bulan)"] = replacement_ratio_min * st.session_state.df.loc[condition_1 & condition_3, "Gapok Terakhir"]
    st.session_state.df.loc[(condition_1 & ~(condition_2 | condition_3)), "Benefit Pensiun Normal Taspen (1 Bulan)"] = pensiun_normal_ratio * st.session_state.df.loc[(condition_1 & ~(condition_2 | condition_3)), "Total Masa Kerja Harapan (MK)"] * st.session_state.df.loc[(condition_1 & ~(condition_2 | condition_3)), "Gapok Terakhir"]

    st.session_state.df["Benefit Pensiun Normal (1 Tahun)"] = st.session_state.df["Benefit Pensiun Normal (1 Bulan)"] * 12
    st.session_state.df["Benefit Pensiun Normal Taspen (1 Tahun)"] = st.session_state.df["Benefit Pensiun Normal Taspen (1 Bulan)"] * 12
    st.session_state.df["Replacement Ratio"] = st.session_state.df["Benefit Pensiun Normal Taspen (1 Bulan)"] / st.session_state.df["Gapok Terakhir"]

# Button to trigger recalculation
if st.button("Calculate"):
    recalculate_variables()

# Display the DataFrame
st.dataframe(st.session_state.df)