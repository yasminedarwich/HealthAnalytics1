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

st.title("Do countries who are unhappy have a higher suicide rate?")
st.write(
    """This page illustrates a combination of plots of countries' suicide data ☠️ """
)

suicide = pd.read_csv('who_suicide_statistics.csv')

#Suicide of top most 10 country
suicide_info=suicide.groupby('country').sum().sort_values(by='suicides_no',ascending=False)[['suicides_no']][:10]
country=["Russian Federation", "United States of America", "Japan", "France", "Ukraine", "Germany", "Republic of Korea", "Brazil", "Poland","United Kingdom"]
suicide_info["country"]=country
fig=px.bar(suicide_info, x="country", y="suicides_no", color_discrete_sequence =['violet'])
fig.update_layout(
    autosize=False,
    width=1000,
    height=600,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ))

st.markdown("<h2 style='text-align: center; color: black;'> Countries with the Highest Suicide Rate</h2>", unsafe_allow_html=True)
st.plotly_chart(fig)


#Total Suicide on each year in descending order
Suicidedata = suicide.groupby("year").sum().sort_values(by='year',ascending=True)[['suicides_no']]
st.markdown("<h2 style='text-align: center; color: black;'> Global Suicide Rates over the Years</h2>", unsafe_allow_html=True)
st.bar_chart(Suicidedata, width=1000, height=400, use_container_width=True)
suicide_country_age = suicide.groupby(['country','age']).sum()['suicides_no'].reset_index()

#Suicide Based on Country And Age
plt.figure()
suicidefig = plt.figure(figsize=(20,40))
sns.stripplot(x='suicides_no',y='country',hue='age',data=suicide_country_age,jitter=True)
plt.ylabel("Country")
plt.xlabel("Suicide Number")
st.markdown("<h2 style='text-align: center; color: black;'> Suicide Based On The Country and Age</h2>", unsafe_allow_html=True)
st.pyplot(suicidefig)

