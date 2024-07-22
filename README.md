https://movie-recommendation-app-wntj6yzrdcmhwlrfxufefy.streamlit.app/
Project Statement: The project is a movie recommendation system that provides the top five similar movies to a selected movie. It also includes a sentiment analysis of the movie reviews.

Goals of the Project:

To recommend top five similar movies to the user-selected movie.
To provide a detailed page for each movie, including cast, brief info, top five related movies, and sentiment-analyzed reviews.
To visually represent the sentiment of the reviews with color-coding: blue for positive and red for negative sentiments.
Project Summary: The project uses a dataset of about 5000 movies scraped from TMDB and converted into a pandas DataFrame. Exploratory Data Analysis (EDA) was performed on the data, and Stem Vectorization was applied to relevant features. TF-IDF Vectorization and Cosine Similarity were used to calculate the similarity between the movies. For sentiment analysis, a dataset of 50000 labeled movie reviews from Kaggle was used, and the Naive Bayes algorithm was applied to predict if a review is positive or negative. The web application was developed using Streamlit and deployed on Streamlit Cloud.

This project not only recommends movies but also provides an interactive and informative platform for users to explore movies and understand the sentiments of the reviews.
