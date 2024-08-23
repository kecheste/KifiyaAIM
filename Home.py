import streamlit as st
import pandas as pd
import plotly.express as px
import os
from app.utils import process_data
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Solar Radiation Measurement Data",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )
st.header('Solar Radiation Measurement Data')

@st.cache_data
def load_data(path:str):
    data = pd.read_csv(path)
    return data

data_dir = "./data"
dataframes = {
    "benin": os.path.join(data_dir, "benin-malanville.csv"),
    "sierra_leone": os.path.join(data_dir, "sierraleone-bumbuna.csv"),
    "togo": os.path.join(data_dir, "togo-dapaong_qc.csv"),
}

available_variables = ['Benin', 'Sierra Leone', 'Togo']
selected_variable = st.selectbox('Select Country', available_variables)

if selected_variable == 'Benin':
    df = load_data(dataframes["benin"]).head(10000)
    st.line_chart(df['GHI'])
    st.header('Summary Statistics')
    st.write(df.describe())
    st.header('Correlation Analysis')
    process_data = process_data(df)
    correlation_matrix = process_data.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    st.pyplot(fig)

elif selected_variable == 'Sierra Leone':
    df = load_data(dataframes["sierra_leone"]).head(10000)
    st.line_chart(df['GHI'])
    st.header('Summary Statistics')
    st.write(df.describe())
    st.header('Correlation Analysis')
    process_data = process_data(df)
    correlation_matrix = process_data.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    st.pyplot(fig)

elif selected_variable == 'Togo':
    df = load_data(dataframes["togo"]).head(10000)
    st.line_chart(df['GHI'])
    st.header('Summary Statistics')
    st.write(df.describe())
    st.header('Correlation Analysis')
    process_data = process_data(df)
    correlation_matrix = process_data.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    st.pyplot(fig)
