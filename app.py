import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('/Users/matt/Car-Sales-Advertisements/Car-Sales-Advertisements/vehicles_us.csv')

# Add a header
st.header('Car Sales Dashboard')

# Add a histogram
if st.checkbox('Show price distribution'):
    fig1 = px.histogram(df, x='price', title='Distribution of Prices')
    st.plotly_chart(fig1)

# Add a scatter plot
fig2 = px.scatter(df, x='odometer', y='price', title='Odometer vs Price')
st.plotly_chart(fig2)
