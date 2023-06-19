import streamlit as st
import pickle
import pandas as pd
import requests

# movies_list = pickle.load(open('movies.pkl','rb'))
movie_list = pd.read_pickle(open('movies.pkl', 'rb'))
similarity = pd.read_pickle(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")


def fetch_poster(movie_id):
    myurl = 'https://api.themoviedb.org/3/movie/{}?api_key=95ba9b1d1e5b4475b3f759f2db4af6bb'.format(movie_id)
    response = requests.get(myurl)
    data = response.json()
    return "https://image.tmdb.org/t/p/original/" + data['poster_path']

def recommend(movie):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[1:6]
    recommended_movies =[]
    recommended_movies_poster =[]
    for i in movies_list:
        movie_id = movie_list.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies.append(movie_list.iloc[i[0]].title)
    return recommended_movies,recommended_movies_poster

selected_movie = st.selectbox(
    'Select a movie',movie_list['title'].values
)

if st.button('Recommend'):
    recommendations,posters = recommend(selected_movie)

    import streamlit as st

    col1, col2, col3,col4,col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])
    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])



    # for i in recommendations:
    #     st.write(i)

