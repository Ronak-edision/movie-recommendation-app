def recommend(movie, movies_df, similarity):
    recommended_movies = []
    recommended_movie_ids = []

    try:
        movie_index = movies_df[movies_df['title'] == movie].index[0]
        movie_language = movies_df.loc[movie_index, 'original_language']

        distances = similarity[movie_index]
        movie_indices = distances.argsort()[::-1][1:]

        language_count = 0

        for idx in movie_indices:
            if movies_df.loc[idx, 'original_language'] == movie_language:
                if language_count < 3:
                    recommended_movies.append(movies_df.loc[idx].title)
                    recommended_movie_ids.append(movies_df.loc[idx].id)
                    language_count += 1
            else:
                recommended_movies.append(movies_df.loc[idx].title)
                recommended_movie_ids.append(movies_df.loc[idx].id)

            if len(recommended_movies) == 5:
                break

    except IndexError:
        st.warning("No similar movies found.")

    return recommended_movies, recommended_movie_ids