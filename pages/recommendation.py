import  streamlit as st

import pickle
import pandas as pd


st.title('Movie Recommender System')


def fetch_poster(movie_id):

    data = pd.read_csv('data.csv')


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movie_posters = []

    for i in movies_list:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movie_posters

data_dict = pickle.load(open('rating'))
data = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)
if st.button('Show Recommendation'):
    names,posters = recommend(selected_movie_name)

    #display with the columns
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])