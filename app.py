from tkinter.font import names

import os

if not os.path.exists("similarity.pkl"):
    import build_model
    
import streamlit as st
import pickle
import pandas as pd
import requests
import os
from dotenv import load_dotenv

# -------------------- CONFIG --------------------

# -------------------- DARK THEME --------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.stApp {
    background-color: #0e1117;
}
.stMarkdown, .stText, p, span {
    color: white !important;
}
h1, h2, h3 {
    color: #e50914 !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------- LOAD ENV --------------------
load_dotenv()
try:
    API_KEY = st.secrets["TMDB_API_KEY"]
except:
    API_KEY = os.getenv("TMDB_API_KEY")
# -------------------- LOAD DATA --------------------
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# -------------------- FAST LOOKUP --------------------
movie_dict = {movie: idx for idx, movie in enumerate(movies['title'])}

# -------------------- FETCH DETAILS --------------------
@st.cache_data
def fetch_movie_details(movie_name):

    try:
        # clean movie name
        movie_name = movie_name.replace(":", "").replace("-", "")

        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
        data = requests.get(url).json()

        results = data.get("results")

        if results and len(results) > 0:

            movie = results[0]

            poster_path = movie.get("poster_path")
            rating = movie.get("vote_average")
            overview = movie.get("overview")

            poster_url = (
                f"https://image.tmdb.org/t/p/w500{poster_path}"
                if poster_path
                else "https://via.placeholder.com/300x450?text=No+Poster"
            )

            return (
                poster_url,
                rating if rating else "N/A",
                overview if overview else "No description available"
            )

        else:
            return (
                "https://via.placeholder.com/300x450?text=Not+Found",
                "N/A",
                "Unable to fetch details"
            )

    except:
        return (
            "https://via.placeholder.com/300x450?text=Error",
            "N/A",
            "Unable to fetch details"
        )
# -------------------- RECOMMEND FUNCTION --------------------
def recommend(movie):

    index = movie_dict.get(movie)

    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:10]   # take more candidates

    names = []
    posters = []
    ratings = []
    overviews = []

    for i in movie_list:

        movie_name = movies.iloc[i[0]].title

        poster, rating, overview = fetch_movie_details(movie_name)

        # only keep valid posters
        if poster and "placeholder" not in poster:

            names.append(movie_name)
            posters.append(poster)
            ratings.append(rating)
            overviews.append(overview)

        # stop at 4 valid movies
        if len(names) == 4:
            break

    return names, posters, ratings, overviews
# -------------------- UI --------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #E50914;'>
    🎬 CineMatch
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>AI Movie Recommendation System</p>",
    unsafe_allow_html=True
)

# -------------------- SEARCH --------------------
selected_movie = st.selectbox(
    "🔍 Search and select a movie",
    movies['title'].values
)

# -------------------- BUTTON --------------------
if st.button("🚀 Recommend"):

    with st.spinner("🍿 Finding best movies for you..."):

        names, posters, ratings, overviews = recommend(selected_movie)

    if names:

        st.markdown("## 🎯 Top Recommendations")

        cols = st.columns(4)

        for i in range(len(names)):
             with cols[i]:
                st.image(posters[i], width=180)
                st.markdown(f"**{names[i]}**")
                st.markdown(f"⭐ {ratings[i]} / 10")
                st.caption(overviews[i][:120] + "...")
                st.markdown("""
                <style>
                .stButton>button {
                    background-color: #e50914;
                    color: white;
                    border-radius: 8px;
                    height: 45px;
                    width: 200px;
                    font-size: 16px;
                    font-weight: bold;
                }

                .stButton>button:hover {
                    background-color: #ff1f1f;
                    color: white;
                }
                </style>
                """, unsafe_allow_html=True)
                                

    else:
        st.error("Something went wrong. Try another movie.")