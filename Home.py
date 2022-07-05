import streamlit as st
from PIL import Image
import plotly.express as px
import numpy as np 
import pandas as pd 
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt

#Homepage configuration

im = Image.open("win.png")

st.set_page_config(
    page_title="World Happiness Report",
    page_icon= im,
    layout="wide",
    initial_sidebar_state="expanded")

hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
header{visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# ---Side-Bar----

with st.sidebar:
    st.write('''
    Hey there! 👋🏻 

    I am Yasmine Darwich, an MSBA student at AUB 👱‍♀️🏫! 

    I enjoy working with datasets and analyzing information 🎯. 
    
    Let's connect:

    [LinkedIn](https://www.linkedin.com/in/yasmine-darwich/)

    [Twitter](https://twitter.com/DonaLeb_)

    [Instagram](https://www.instagram.com/dona.leb/)

    ''')
    st.write("---")

st.title("Analyzing the World Happiness Report alongside Alcohol Consumption & Suicide Rates")

st.markdown(
        """
        #### The main objective of this report is to understand how happiness relates to socio-economic factors, what are the countries that lead the rankings for happiness and what makes them stand out with respect to the rest. Additionally, we will be utilizing suicide rates data and alcohol consumption data not to discuss the reason behind the happiness rates of a specific country but to try to understand the effects of an unhappy country.
        """
    )

st.info(
        """
        👈 Click on the left sidebar menu to navigate to the different visualizations! 
        """
    )

st.markdown(
        """
        *The data used for this project was initiated by WHO (World Health Organization) and downloaded from Kaggle: the World Happines Report (2015 - 2021), alcoholic consumption from the Global Information System on Alcohol (2010) and suicide rates (1979 - 2016)*
        """
    )


from PIL import Image
image = Image.open('Happy .jpeg')
col1, col2, col3 = st.columns([0.2, 5, 0.2])
col2.image('Happy .jpeg', use_column_width=True)


data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])
if data is not None:
        df = pd.read_csv(data)
        st.dataframe(df.head())
                        

if st.checkbox("Show Shape"):
        st.write(df.shape)

if st.checkbox("Show Columns"):
        all_columns = df.columns.to_list()
        st.write(all_columns)

if st.checkbox("Summary"):
        st.write(df.describe())

if st.checkbox("Show Selected Columns"):
        all_columns = df.columns.to_list()
        selected_columns = st.multiselect("Select Columns",all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)

if st.checkbox("Show Value Counts"):
        st.write(df.iloc[:,-1].value_counts())



    