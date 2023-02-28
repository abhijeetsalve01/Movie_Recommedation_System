import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from numpy import random
st.set_page_config(page_title='Search System',
                   layout='wide')
st.title('Search System')
st.header("->Select the Year, Genre, Rating From The Menu For Searching In Database:clapper:")
#Search the Dataset
df = pd.read_csv('data.csv')
st.write(df)

#Search
df = df.drop(columns=["year","certificate",'description','stars','votes','duration','rating']).dropna(axis=0)

random.seed(1)
df["id"] = [i for i in range(100000,100000+len(df.values))]
df.set_index(df["id"],inplace=True)
df.drop("id",inplace=True,axis=1)

df["genre"] = df["genre"].str.split(',')
for index,series in df.iterrows():
    for genre in series["genre"]:
        df.at[index,genre.strip()] = 1

df.fillna(0, inplace=True)

df.drop_duplicates(subset="title",inplace=True)

st.write(df.head(4))


def user_profiler(data_dictionary, movies_matrix):
    mov_mat = []
    rate_mat = []
    for (movie, rate) in zip(data_dictionary.keys(), data_dictionary.values()):
        rate_mat.append(pd.Series(rate))
        mov_mat.append(movies_matrix.iloc[movies_matrix.index[movies_matrix["title"] == movie][0] - 100000][2:])

    mov_mat = pd.DataFrame(mov_mat, columns=movies_matrix.columns[2:])
    rate_mat = pd.DataFrame(rate_mat)
    mov_mat = mov_mat.fillna(0)
    rate_mat = rate_mat.to_numpy().transpose()
    user_p = rate_mat @ mov_mat
    # Normalizing:
    user_p = user_p / user_p.max(axis=1)[0]
    return user_p


def recommender(user_profile, movies_matrix, number_of_recommends=2):
    transposed_mov_mat = pd.DataFrame(movies_matrix.T.values[2:, :]).to_numpy().transpose()
    transposed_user_p = user_profile.to_numpy().transpose()
    recommended_movies = transposed_mov_mat @ transposed_user_p
    recommended_movies = pd.DataFrame(recommended_movies, movies_matrix['title'])
    recommended_movies.sort_values(by=[0], inplace=True, ascending=False)
    recommended_movies = recommended_movies[:number_of_recommends]

    return recommended_movies
