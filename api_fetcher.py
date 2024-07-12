import requests

# Function to fetch movie posters
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path if poster_path else None
    return full_path

# Function to fetch movie details
def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    return data
# Function to fetch movie cast
# Function to fetch movie cast
def fetch_movie_cast(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    cast = data['cast'][:5]  # Limit to top 5 cast members
    cast_details = []
    for member in cast:
        profile_path = member['profile_path']
        profile_url = "https://image.tmdb.org/t/p/w500/" + profile_path if profile_path else None
        cast_details.append({
            'name': member['name'],
            'profile_url': profile_url
        })
    return cast_details