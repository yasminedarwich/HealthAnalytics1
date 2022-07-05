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

#Data viz and analysis
happiness_2k15 = pd.read_csv('2015.csv')
happiness_2k16 = pd.read_csv('2016.csv')
happiness_2k17 = pd.read_csv('2017.csv')
happiness_2k18 = pd.read_csv('2018.csv')
happiness_2k19 = pd.read_csv('2019.csv')
happiness_2k20 = pd.read_csv('2020.csv')
happiness_2k21 = pd.read_csv('world-happiness-report-2021.csv')

st.title('What is affecting the happiness of a country?')

happiness_2k18['Perceptions of corruption'] = happiness_2k18['Perceptions of corruption'].fillna(0) #1na value was represented here
st.write(
    """This page illustrates a combination of plots and animations related to every countries' happiness data and features affecting their happiness! Enjoy 🎉"""
)


#Renaming columns of all data
happiness_2k15.rename(columns = {'Economy (GDP per Capita)':'GDP per Capita', 'Health (Life Expectancy)':'Healthy Life Expectancy'},inplace = True)
happiness_2k16.rename(columns = {'Economy (GDP per Capita)':'GDP per Capita', 'Health (Life Expectancy)':'Healthy Life Expectancy'},inplace = True)
happiness_2k17.rename(columns = {'Economy..GDP.per.Capita.':'GDP per Capita', 'Health..Life.Expectancy.':'Healthy Life Expectancy', 'Happiness.Score':'Happiness Score'},inplace = True)
happiness_2k18.rename(columns = {'GDP per capita':'GDP per Capita', 'Healthy life expectancy':'Healthy Life Expectancy', 'Score':'Happiness Score'},inplace = True)
happiness_2k18.rename(columns = {'Country or region':'Country'},inplace = True)
happiness_2k19.rename(columns = {'Country or region':'Country'},inplace = True)
happiness_2k19.rename(columns = {'GDP per capita':'GDP per Capita', 'Healthy life expectancy':'Healthy Life Expectancy','Score':'Happiness Score'},inplace = True)
happiness_2k20.rename(columns = {'Logged GDP per capita':'GDP per Capita', 'Healthy life expectancy':'Healthy Life Expectancy','Ladder score':'Happiness Score'},inplace = True)
happiness_2k21.rename(columns = {'Logged GDP per capita':'GDP per Capita', 'Healthy life expectancy':'Healthy Life Expectancy','Ladder score':'Happiness Score'},inplace = True)
happiness_2k20.rename(columns = {'Country name':'Country'},inplace = True)
happiness_2k21.rename(columns = {'Country name':'Country'},inplace = True)

# Adding a new "Year" Column

happiness_2k15['Year'] = 2015
happiness_2k16['Year'] = 2016
happiness_2k17['Year'] = 2017
happiness_2k18['Year'] = 2018
happiness_2k19['Year'] = 2019
happiness_2k20['Year'] = 2020
happiness_2k21['Year'] = 2021

happiness_2015=happiness_2k15[['Country', 'Year','Happiness Score','GDP per Capita','Healthy Life Expectancy']]
happiness_2016=happiness_2k16[['Country', 'Year','Happiness Score','GDP per Capita','Healthy Life Expectancy']]
happiness_2017=happiness_2k17[['Country', 'Year','Happiness Score','GDP per Capita','Healthy Life Expectancy']]
happiness_2018=happiness_2k18[['Country', 'Year','Happiness Score','GDP per Capita','Healthy Life Expectancy']]
happiness_2019=happiness_2k19[['Country', 'Year','Happiness Score','GDP per Capita','Healthy Life Expectancy']]
happiness_2020=happiness_2k20[['Country', 'Year','Happiness Score','GDP per Capita','Healthy Life Expectancy']]
happiness_2021=happiness_2k21[['Country', 'Year','Happiness Score','GDP per Capita','Healthy Life Expectancy']]

# Merging all years into one dataframe
    
happiness_data = pd.concat([happiness_2015, happiness_2016,happiness_2017,happiness_2018,happiness_2019,happiness_2020,happiness_2021])

top5 = happiness_2k21.groupby('Country')['Happiness Score'].max().sort_values(ascending=False).head(5).reset_index()
lower5 = happiness_2k21.groupby('Country')['Happiness Score'].max().sort_values(ascending=False).tail(5).reset_index()
rank_data = pd.concat([top5,lower5],axis=0)
rank_data.columns = ['Country','Score']

row1,row2 =st.columns(2)

with row1:
    data = dict(
        type = 'choropleth',
        marker_line_width=1,
        locations = happiness_2k15['Country'],
        locationmode = "country names",
        z = happiness_2k21['Happiness Score'],
        text = happiness_2k15['Country'],
        colorbar = {'title' : 'Happiness score'})
    choromap = go.Figure(data = [data])
#layout = dict(title = 'Happiness Map for the year 2021',geo = dict(projection = {'type':'mercator'}))
    st.write('### Happiness Map for the year 2021')
    st.plotly_chart(choromap)

with row2:
    fig = px.bar(rank_data, x="Score", y="Country", orientation='h',color='Score')
    st.write('### Top 5 Happiest & Saddest Countries')
    st.plotly_chart(fig)



metric_list = ['GDP per Capita', 'Social support', 'Healthy Life Expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']

all_columns_names = metric_list
type_of_plot = "Correlation map"
selected_columns_names = st.selectbox("Select Columns To plot",all_columns_names)

if st.button("Generate Plot"):
     st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

fig2= px.scatter(happiness_2k21, x='Happiness Score', y=selected_columns_names,
           size="Happiness Score", color="Country", hover_name="Country",
           trendline= "ols")
st.markdown("<h2 style='text-align: center; color: black;'> Correlation graph showing how the happiness of a country is affected by the different variables </h2>", unsafe_allow_html=True)
st.write(
    """This demo illustrates a combination of features by WHO affecting a country's happiness such as GDP per capita, social support, healthy life expectancy, freedom to make life choices, generosity, perceptions of corruption for 2021!"""
)
st.plotly_chart(fig2,use_container_width=True)


# Plotting freedom life of choices  of top 30 countries from 2015-2021 through plotly

df2015 = happiness_2k15.iloc[:30,:]
df2016 = happiness_2k16.iloc[:30,:]
df2017 = happiness_2k17.iloc[:30,:]
df2018 = happiness_2k18.iloc[:30,:]
df2019 = happiness_2k19.iloc[:30,:]
df2020 = happiness_2k20.iloc[:30,:]
df2021 = happiness_2k21.iloc[:30,:]


st.markdown("<h2 style='text-align: center; color: black;'> Freedom of life of choices for the top 30 countries from 2015-2021 </h2>", unsafe_allow_html=True)

# Creating curve1

curve1 = go.Scatter(x = df2015['Country'],
                    y = df2015['Freedom'],
                    mode = "lines+markers",
                    name = "2015",
                    marker = dict(color = 'red'),
                    text= df2015.Country)

# Creating curve2
curve2 = go.Scatter(x = df2015['Country'],
                    y = df2016['Freedom'],
                    mode = "lines+markers",
                    name = "2016",
                    marker = dict(color = 'blue'),
                    text= df2015.Country)

# Creating curve3
curve3 = go.Scatter(x = df2015['Country'],
                    y = df2017['Freedom'],
                    mode = "lines+markers",
                    name = "2017",
                    marker = dict(color = 'green'),
                    text= df2015.Country)

# Creating curve4
curve4 = go.Scatter(x = df2015['Country'],
                    y = df2018['Freedom to make life choices'],
                    mode = "lines+markers",
                    name = "2018",
                    marker = dict(color = 'black'),
                    text= df2015.Country)

# Creating curve5
curve5 = go.Scatter(x = df2015['Country'],
                    y = df2019['Freedom to make life choices'],
                    mode = "lines+markers",
                    name = "2019",
                    marker = dict(color = 'pink'),
                    text= df2015.Country)

# Creating curve6
curve6 = go.Scatter(x = df2015['Country'],
                    y = df2020['Freedom to make life choices'],
                    mode = "lines+markers",
                    name = "2020",
                    marker = dict(color = 'purple'),
                    text= df2015.Country)

# Creating curve7
curve7 = go.Scatter(x = df2015['Country'],
                    y = df2021['Freedom to make life choices'],
                    mode = "lines+markers",
                    name = "2021",
                    marker = dict(color = 'orange'),
                    text= df2015.Country)

data = [curve1, curve2, curve3, curve4, curve5,curve6,curve7]
layout = dict(title = 'Freedom score of top 30 countries from 2015 to 2021',
              xaxis= dict(title= 'Countries'),
              yaxis= dict(title= 'Freedom'),
              hovermode="x unified"
             )

fig = dict(data = data, layout = go.Layout(
    autosize=False,
    width=1300,
    height=500,
    margin=dict(t=50, b=50, r=50, l=50)
))
st.plotly_chart(fig)

st.markdown("<h2 style='text-align: center; color: black;'> Happiness score of the top 30 countries from 2015-2021 </h2>", unsafe_allow_html=True)


# Plotting happiness of top 30 countries from 2015-2021 through plotly

df2015 = happiness_2k15.iloc[:30,:]
df2016 = happiness_2k16.iloc[:30,:]
df2017 = happiness_2k17.iloc[:30,:]
df2018 = happiness_2k18.iloc[:30,:]
df2019 = happiness_2k19.iloc[:30,:]
df2020 = happiness_2k20.iloc[:30,:]
df2021 = happiness_2k21.iloc[:30,:]


# Creating curve1

curve1 = go.Scatter(x = df2015['Country'],
                    y = df2015['Happiness Score'],
                    mode = "lines+markers",
                    name = "2015",
                    marker = dict(color = 'red'),
                    text= df2015.Country)

# Creating curve2
curve2 = go.Scatter(x = df2015['Country'],
                    y = df2016['Happiness Score'],
                    mode = "lines+markers",
                    name = "2016",
                    marker = dict(color = 'blue'),
                    text= df2015.Country)

# Creating curve3
curve3 = go.Scatter(x = df2015['Country'],
                    y = df2017['Happiness Score'],
                    mode = "lines+markers",
                    name = "2017",
                    marker = dict(color = 'green'),
                    text= df2015.Country)

# Creating curve4
curve4 = go.Scatter(x = df2015['Country'],
                    y = df2018['Happiness Score'],
                    mode = "lines+markers",
                    name = "2018",
                    marker = dict(color = 'black'),
                    text= df2015.Country)

# Creating curve5
curve5 = go.Scatter(x = df2015['Country'],
                    y = df2019['Happiness Score'],
                    mode = "lines+markers",
                    name = "2019",
                    marker = dict(color = 'pink'),
                    text= df2015.Country)

# Creating curve6
curve6 = go.Scatter(x = df2015['Country'],
                    y = df2020['Happiness Score'],
                    mode = "lines+markers",
                    name = "2020",
                    marker = dict(color = 'purple'),
                    text= df2015.Country)

# Creating curve7
curve7 = go.Scatter(x = df2015['Country'],
                    y = df2021['Happiness Score'],
                    mode = "lines+markers",
                    name = "2021",
                    marker = dict(color = 'orange'),
                    text= df2015.Country)

data = [curve1, curve2, curve3, curve4, curve5,curve6,curve7]
layout = dict(title = 'Happiness score of top 30 countries from 2015 to 2021',
              xaxis= dict(title= 'Countries'),
              yaxis= dict(title= 'Happiness Score'),
              hovermode="x unified"
             )

fig = dict(data = data,layout = go.Layout(
    autosize=False,
    width=1300,
    height=500,
    margin=dict(t=50, b=50, r=50, l=50)
))
st.plotly_chart(fig)

fig4, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 6), sharey='row', sharex='row')

axes[0, 0].scatter(x=happiness_2k21['GDP per Capita'], y=happiness_2k21['Happiness Score'])
axes[0, 0].set_xlabel('GDP per capita')
axes[0, 0].set_ylabel('Happiness score')

axes[0, 1].scatter(x=happiness_2k21['Social support'], y=happiness_2k21['Happiness Score'])
axes[0, 1].set_xlabel('Social Support')
axes[0, 1].set_ylabel('Happiness score')

axes[1, 0].scatter(x=happiness_2k21['Explained by: Healthy life expectancy'], y=happiness_2k21['Happiness Score'])
axes[1, 0].set_xlabel('Healthy life expectancy')
axes[1, 0].set_ylabel('Happiness score')

axes[1, 1].scatter(x=happiness_2k21['Explained by: Freedom to make life choices'], y=happiness_2k21['Happiness Score'])
axes[1, 1].set_xlabel('Freedom To Make Life Choices')
axes[1, 1].set_ylabel('Happiness score')

axes[2, 0].scatter(x=happiness_2k21['Explained by: Perceptions of corruption'],y=happiness_2k21['Happiness Score'])
axes[2, 0].set_xlabel('Perceptions of Corruption')
axes[2, 0].set_ylabel('Happiness score')

axes[2, 1].scatter(x=happiness_2k21['Explained by: Generosity'], y=happiness_2k21['Happiness Score'])
axes[2, 1].set_xlabel('Generosity')
axes[2, 1].set_ylabel('Happiness score')
fig4.tight_layout()

st.markdown("<h2 style='text-align: center; color: black;'> Happiness & what affects it </h2>", unsafe_allow_html=True)
st.pyplot(fig4)


fig5 = px.sunburst(happiness_2k21, path=['Regional indicator', 'Country'], values='Happiness Score',
                  color='Happiness Score',
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(happiness_2k21['Happiness Score'], weights=happiness_2k21['Happiness Score']))
fig5.update_layout(
    autosize=False,
    width=1000,
    height=1000,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ))
st.markdown("<h2 style='text-align: center; color: black;'> Happiness per Region & Country </h2>", unsafe_allow_html=True)
st.plotly_chart(fig5)


# Plotting heatmap of the data to show correlation between various features

dcr = happiness_2k21.drop(['Standard error of ladder score', 'Year', 'GDP per Capita','upperwhisker', 'lowerwhisker','Ladder score in Dystopia',
       'Explained by: Social support',
       'Explained by: Healthy life expectancy',
       'Explained by: Freedom to make life choices',
       'Explained by: Generosity', 'Explained by: Perceptions of corruption',
        'Dystopia + residual'],axis=1)
cor = dcr.corr() #Calculate the correlation of the above variables
fig3 = plt.figure()
fig3happiness = plt.figure(figsize=(2,2))
sns.heatmap(cor.corr(), square = True) #Plot the correlation as heat map
st.markdown("<h2 style='text-align: center; color: black;'> Correlation Features of Happiness for 2021</h2>", unsafe_allow_html=True)
sns.set(font_scale=0.5)
st.pyplot(fig3happiness)



