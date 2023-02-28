import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import time 
import plotly.express as px
import seaborn as sns
from PIL import Image

st.set_page_config(
    page_title="Data Visualization Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

#Dashboard Title
st.title('Data Visualization Dashboard')

# The Dataset path
df = pd.read_csv("data.csv")

#Display_the _raw_data
st.markdown("Displaying Data table")
st.dataframe(df)
df.head(10)
st.markdown("---------------------------------------------------------------------------")

#showing only limited data
st.markdown("First Four Rows")
st.write(df.head())

st.markdown("---------------------------------------------------------------------------")

st.markdown('To find no. of rows and columns')
st.write(df.shape)

st.markdown("---------------------------------------------------------------------------")

st.markdown("Finding the Null/Missing")
st.write(df.isnull().sum())

st.markdown("---------------------------------------------------------------------------")

#Second Table
st.markdown("Recommendation Engine using type, country and genres")
st.write(df[['title','year','genre','rating']])

st.markdown("---------------------------------------------------------------------------")

#displaying the data movies or series
st.markdown("Displaying the data movies or series")
st.write(df['genre'].value_counts())

st.markdown("---------------------------------------------------------------------------")

#data management
genre_option = df['genre'].unique().tolist()
genre = st.selectbox('The types of genre available', genre_option, 0)
df = df[df['genre']==genre]
st.write(df)

st.markdown("---------------------------------------------------------------------------")

st.markdown('Dataset Summary')
st.write(df.describe())

st.markdown("---------------------------------------------------------------------------")

st.markdown('Sorting rating')
st.write(df.sort_values('rating'))

st.markdown("---------------------------------------------------------------------------")

st.markdown('sorting according to rating highest to lowest')
st.write(df.sort_values("rating",ascending=False))

st.markdown("---------------------------------------------------------------------------")

st.markdown('Top 10 highest rated Netflix series')
top_10 = df.sort_values("rating",ascending=False).head(20)
st.write(top_10)

st.markdown("---------------------------------------------------------------------------")

#Plotting
st.markdown('Year Wise Title Released')
image = Image.open('year_wise_data.png')
st.image(image, caption='Year Wise Title Released')