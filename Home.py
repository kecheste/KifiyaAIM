import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Solar Radiation Measurement Data",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )
st.title("Solar Radiation Measurement Data")

@st.cache_data
def load_data(path:str):
    data = pd.read_csv(path)
    return data

data_dir = "./data"
file_paths = {
    "benin": os.path.join(data_dir, "benin-malanville.csv"),
    "sierra_leone": os.path.join(data_dir, "sierraleone-bumbuna.csv"),
    "togo": os.path.join(data_dir, "togo-dapaong_qc.csv"),
}

df = load_data(file_paths["benin"]).head(1000)

col1, col2, col3 = st.columns([1,1,1])

radiation_data = df

with col1.expander("Radiation Data"):
    st.dataframe(df)

info = df.describe()

with col2.expander("Description"):
    st.write(info)

with col3.expander("Average Radiation"):
    st.write(info["GHI"].mean())

col3.metric(label="Prediction", value= '{:,.2}'.format(info["GHI"].mean()))

@st.cache_data
def scatter_plot():
    fig = px.scatter(df, x="Timestamp", y="GHI", title="GHI With Time")
    st.plotly_chart(fig, use_container_width=True)

with col1:
    scatter_plot()

@st.cache_data
def line_plot():
    fig = px.line(radiation_data, x="Timestamp", y="GHI", color="WS",text= "WS", markers=True,
                  title="GHI vs Wind Speed")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    line_plot()


# Pie chart
@st.cache_data
def pie_plot():
    fig = px.pie(df, names="WS", values="WS", title="GHI Distribution")
    st.plotly_chart(fig, use_container_width=True)

with col3:
    pie_plot()

# Bar chart
@st.cache_data
def bar_plot():
    fig = px.bar(radiation_data, x="Timestamp", y="GHI", color="WS", title="Daily GHI vs Wind Speed")
    st.plotly_chart(fig, use_container_width=True)  

with col1:
    bar_plot()

