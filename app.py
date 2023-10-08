import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    # this will use movie id for getting its details, poster apparantely is what we want
    response = requests.get('https://api.themoviedb.org/3/movie/{}?&append_to_response=videos&api_key=f5748cc54f2d9242c014497a5478c8f5'.format(movie_id))
    data = response.json()
    #st.text(data)
    #st.text('https://api.themoviedb.org/3/movie/{}?&append_to_response=videos&api_key=f5748cc54f2d9242c014497a5478c8f5'.format(movie_id))
    #print(data)
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]  # similarity vector for particular movie from index
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for j in movies_list:
        movie_id = movies.iloc[j[0]].movie_id
        recommended_movies.append(movies.iloc[j[0]].title)
        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

movies = pickle.load(open('movies.pkl', 'rb')) # oepning movies.pkl in read binary mode and loaded into this variable
# dataframe and we are extraction only title array from it

st.title('Movie Recommender System')

similarity = pickle.load(open('similarity.pkl', 'rb'))
# this is select box in which we will write movies names for that names we have used pickle library
selected_movie_name = st.selectbox(
'Enter a movie name and get recommendations!',
(movies['title'].values))


# recommend button clicking by which you will get a list of recommended movies
if st.button('Recommed'):
    names,posters = recommend(selected_movie_name) # getting movie names ans posters

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

# now we need movies posters along with name
# procfile is for running this on heroku server also setup.sh