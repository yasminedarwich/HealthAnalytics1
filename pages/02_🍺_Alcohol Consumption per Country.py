import streamlit as st
import plotly.express as px
import numpy as np 
import pandas as pd 
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt

alcohol = pd.read_csv('drinks.csv')

st.title("Do unhappier countries drink more?")
st.write(
    """This page illustrates a combination of plots of countries' alcohol consumption 🍺 """)

total_consumption = alcohol.groupby(['country', 'beer_servings', 'spirit_servings', 'wine_servings']).total_litres_of_pure_alcohol.sum().sort_values(ascending = False).reset_index()
new_total_consumption = total_consumption.head(20)

fig = px.bar(new_total_consumption, 
              x = 'country', 
              y = 'total_litres_of_pure_alcohol', 
              hover_data = ['spirit_servings', 'beer_servings', 'wine_servings'],
              text_auto='.3s',
              height = 600,
              width = 1200,
              color_discrete_sequence =['orange'])
fig.update_traces(textfont_size = 10, 
                  textangle = 0, 
                  textposition = "inside")

st.markdown("<h2 style='text-align: center; color: black;'> Total Consumption of Alcohol by Country </h2>", unsafe_allow_html=True)

st.plotly_chart(fig)


fig1 = px.histogram(alcohol, 'total_litres_of_pure_alcohol',             
                   color="country")

fig1.add_vline(x=alcohol['total_litres_of_pure_alcohol'].mean(), line_width=2, line_dash="dash", line_color="black")
fig1.update_layout(
    autosize=False,
    width=1200,
    height=1000,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ))
st.markdown("<h2 style='text-align: center; color: black;'> Average Alcohol Consumption per Country </h2>", unsafe_allow_html=True)

st.plotly_chart(fig1)


fig3=px.choropleth(data_frame=alcohol,locations='country',locationmode='country names', color='total_litres_of_pure_alcohol'
                  )
fig3.update_layout(
    autosize=False,
    width=1200,
    height=1000,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ))
st.markdown("<h2 style='text-align: center; color: black;'> Map showing the countries' total alcohol consumption </h2>", unsafe_allow_html=True)

st.plotly_chart(fig3)
