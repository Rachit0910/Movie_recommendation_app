# 🎬 Movie Recommendation System

A content-based movie recommendation system built using Python, Pandas, Scikit-Learn, and Streamlit. The application recommends movies similar to a selected movie by analyzing movie metadata such as genres, keywords, cast, and overview.

## Features

* Recommend similar movies based on content similarity
* Interactive web interface built with Streamlit
* Fast recommendation generation using cosine similarity
* Movie poster integration using TMDB API
* Clean and user-friendly UI

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Pickle
* TMDB API

## Project Structure

text
Movie-Recommendation-System/
│
├── app.py
├── movie_dict.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
└── notebooks/

## How It Works

1. Movie data is preprocessed and transformed into textual features.
2. Features are combined into a single representation for each movie.
3. Vectorization techniques are used to convert text into numerical form.
4. Cosine similarity is computed between movies.
5. The system returns the most similar movies for the selected title.

## Installation

Clone the repository:
git clone https://github.com/Rachit0910/Movie_recommendation.model.git


Move into the project directory:
cd Movie_recommendation.model


Install dependencies:
pip install -r requirements.txt


Run the application:
streamlit run app.py

## Future Improvements

* Hybrid recommendation system
* User authentication
* Personalized recommendations
* Movie trailers integration
* Enhanced UI/UX

## Author

Rachit Mishra
