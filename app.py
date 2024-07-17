import streamlit as st
import pickle as pkl
from sentiment import *
from api_fetcher import *
from recommender import *
import requests
from nltk.corpus import stopwords

# Ensure NLTK stopwords are available
try:
    _ = stopwords.words('english')
except LookupError:
    st.error("NLTK stopwords corpus is missing. Please run setup_nltk.py to download it.")

# Load the data
try:
    movies_df = pkl.load(open('movies1.pkl', 'rb'))
    similarity = pkl.load(open('similarity1.pkl', 'rb'))
except FileNotFoundError as e:
    st.error(f"File not found: {e}")
    st.stop()

movies_list = movies_df['title'].values

# Streamlit app
st.title('Movie Recommender System')

# Check if a movie_id is provided in the URL parameters
query_params = st.experimental_get_query_params()
selected_movie_id = query_params.get("movie_id", None)

# Movie Details Page
if selected_movie_id:
    movie_id = int(selected_movie_id[0])
    movie_details = fetch_movie_details(movie_id)
    cast_details = fetch_movie_cast(movie_id)

    st.header(movie_details['title'])
    poster_url = fetch_poster(movie_id)
    if poster_url:
        st.image(poster_url)
    st.write(movie_details['overview'])
    st.write(f"Genres: {', '.join([genre['name'] for genre in movie_details['genres']])}")
    st.write(f"Release date: {movie_details['release_date']}")
    st.write(f"Runtime: {movie_details['runtime']} minutes")
    st.write(f"Rating: {movie_details['vote_average']}/10")
    st.write(f"Votes: {movie_details['vote_count']}")

    # Cast section
    st.header("Cast")
    cols = st.columns(5)
    for idx, member in enumerate(cast_details[:5]):  # Limit to first 5 cast members
        with cols[idx]:
            if member['profile_url']:
                st.image(member['profile_url'], width=100)
            st.write(member['name'])

    # Recommendation section
    st.header("Recommended Movies")
    recommended_movie_names, recommended_movie_ids = recommend(movie_details['title'].lower(), movies_df, similarity)

    cols = st.columns(5)
    for idx, (name, movie_id) in enumerate(zip(recommended_movie_names, recommended_movie_ids)):
        with cols[idx]:
            poster_url = fetch_poster(movie_id)
            if poster_url:
                st.markdown(f"[![{name}]({poster_url})](?movie_id={movie_id})", unsafe_allow_html=True)

    # Fetch reviews for the movie
    url_reviews = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews?api_key=YOUR_API_KEY&language=en-US&page=1"
    response = requests.get(url_reviews)
    if response.status_code == 200:
        reviews = response.json().get('results', [])[:5]  # Limit to first 5 reviews
        if reviews:
            st.write("**Reviews:**")
            for i, review in enumerate(reviews, start=1):
                sentiment = evaluate_sentiment(review['content'])
                color = 'blue' if sentiment == 'positive' else 'red'
                st.markdown(f"{i}. <span style='color: {color};'>{review['content']}</span>", unsafe_allow_html=True)
                st.markdown(f"  Sentiment: <span style='color: {color};'>{sentiment.capitalize()}</span>", unsafe_allow_html=True)
        else:
            st.write("No reviews available.")
    else:
        st.write("Failed to fetch reviews.")

    if st.button("Go Back"):
        st.experimental_set_query_params()

# Recommendation Page
else:
    selected_movie_name = st.selectbox(
        "Select a movie to get recommendations",
        movies_list
    )

    st.write("You selected:", selected_movie_name)

    if st.button("Recommend"):
        recommended_movie_names, recommended_movie_ids = recommend(selected_movie_name, movies_df, similarity)

        cols = st.columns(5)
        for idx, (name, movie_id) in enumerate(zip(recommended_movie_names, recommended_movie_ids)):
            with cols[idx]:
                poster_url = fetch_poster(movie_id)
                if poster_url:
                    st.markdown(f"[![{name}]({poster_url})](?movie_id={movie_id})", unsafe_allow_html=True)
