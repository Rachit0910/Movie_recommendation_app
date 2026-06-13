import os
import streamlit as st
import pickle
import pandas as pd
import requests

def get_api_key():
    try:
        return st.secrets["TMDB_API_KEY"]
    except Exception:
        key = os.environ.get("TMDB_API_KEY")
        if key:
            return key
        st.error(
            "⚠️ TMDB API key not found. "
            "Add it to `.streamlit/secrets.toml` as `TMDB_API_KEY = 'your_key'` "
            "or set the environment variable `TMDB_API_KEY`."
        )
        st.stop()



def fetch_poster(movie_id, api_key):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return None
        data = response.json()
        poster_path = data.get("poster_path")
        if not poster_path:
            return None
        return "https://image.tmdb.org/t/p/w500" + poster_path
    except requests.RequestException:
        return None



def recommend(movie, api_key):
    try:
        movie_index = movies[movies["title"] == movie].index[0]
    except IndexError:
        st.error(f"Movie '{movie}' not found in the dataset.")
        return [], []

    distances = similarity[movie_index]
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1],
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id, api_key))

    return recommended_movies, recommended_posters


# ── Load data ────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    movie_dict = pickle.load(open("movie_dict.pkl", "rb"))
    movies_df = pd.DataFrame(movie_dict)
    sim = pickle.load(open("similarity.pkl", "rb"))
    return movies_df, sim


# ── App ──────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide",
)

st.title("🎬 Movie Recommendation System")
st.markdown("*Powered by content-based filtering · TMDB data*")

api_key = get_api_key()

try:
    movies, similarity = load_data()
except FileNotFoundError as e:
    st.error(
        f"Missing file: **{e.filename}**. "
        "Make sure `movie_dict.pkl` and `similarity.pkl` are in the project root. "
        "Re-run the notebook to regenerate them."
    )
    st.stop()

selected_movie_name = st.selectbox(
    "Choose a movie you like:",
    movies["title"].values,
)

if st.button("🔍 Recommend", use_container_width=False):
    with st.spinner("Finding similar movies..."):
        names, posters = recommend(selected_movie_name, api_key)

    if names:
        st.subheader("You might also like:")
        cols = st.columns(5)
        for col, name, poster in zip(cols, names, posters):
            with col:
                st.text(name)
                if poster:
                    st.image(poster, use_column_width=True)
                else:
                    st.image(
                        "https://via.placeholder.com/500x750?text=No+Poster",
                        use_column_width=True,
                    )