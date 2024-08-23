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

df = load_data(file_paths["benin"])

col1, col2, col3 = st.columns([1,1,1])

# Adding a filter for software sales
# all_months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

# radiation_data = df

# sales_data = df.loc[(df["Year"] == 2023) & 
#             (df["Account"]=="Sales")&
#             (df["business_unit"] =="Software"),
#             ["Scenario"] + all_months,
#             ].melt(
#                 id_vars="Scenario",
#                 var_name="month",
#                 value_name= "sales",
#             )

with col1.expander("Radiation Data"):
    st.dataframe(df)

info = df.describe()

with col2.expander("Description"):
    st.write(info)

# col3.metric(label="Prediction", value= '${:,.2}'.format(info["GHI"].mean()))

#scatter plot
@st.cache_data
def scatter_plot():
    fig = px.scatter(df, x="time", y="GHI", color="Scenario", title="GHI With Time")
    st.plotly_chart(fig, use_container_width=True)

with col1:
    scatter_plot()

# @st.cache_data
# def line_plot():
#     fig = px.line(sales_data, x="month", y="sales", color="Scenario",text= "sales", markers=True,
#                   title="Monthly Budget vs Forecast 2023")
#     st.plotly_chart(fig, use_container_width=True)

# with col2:
#     line_plot()


# # Pie chart
# @st.cache_data
# def pie_plot():
#     fig = px.pie(df, names="Account")
#     st.plotly_chart(fig, use_container_width=True)

# with col3:
#     pie_plot()

# # Bar chart
# @st.cache_data
# def bar_plot():
#     fig = px.bar(sales_data, x="month", y="sales", color="Scenario", title="Monthly Budget vs Forecast 2023")
#     st.plotly_chart(fig, use_container_width=True)  

# with col1:
#     bar_plot()

