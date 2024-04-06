import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
from datetime import datetime

# Assuming you have the necessary data and variables defined (company_list, tech_list, etc.)
df = pd.read_csv("stock_market.csv")

st.title("Closing Price Line Chart by Harshrajsinh Vaghela") 


def filter_data(company_name):
    return df[df["company_name"] == company_name]


# User input for company name
selected_company = st.selectbox(
    "Select Company", ["APPLE", "MICROSOFT", "AMAZON", "GOOGLE"]
)

# Filtered data based on selected company
filtered_df = filter_data(selected_company)

# Plotting
st.title(f"Closing Price Line Chart for {selected_company}")
st.line_chart(filtered_df["Close"])


st.title("Sales Volume Line Chart")

filtered_df = filter_data(selected_company)

# Plotting
st.title(f"Sales Volume Line Chart for {selected_company}")
st.line_chart(filtered_df["Volume"])


closing_info = df.loc[df["company_name"] == selected_company, "Close"].pct_change()

st.title("Daily Return Line Chart")

st.title(f"Daily Return Line Chart for {selected_company}")
st.line_chart(closing_info)
