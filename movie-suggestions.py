from google.cloud import storage
import pandas as pd
from sqlalchemy import create_engine
from sklearn.metrics.pairwise import cosine_similarity
import random

# Google Cloud Storage: Load Movie Metadata because the database file is uploaded to Google Cloud's bucket - datalake
storage_client = storage.Client()
bucket_name = 'movie-datalake'
file_name = 'MovieGenre.csv'
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(file_name)
blob.download_to_filename('MovieGenre.csv')
movies_df = pd.read_csv('MovieGenre.csv', encoding='ISO-8859-1')

# Google Cloud SQL: To connect to the database stored on Google Cloud SQL
db_user = 'root'
db_pass = 'password'
db_name = 'Movies'
db_host = '35.185.85.110'
engine = create_engine(f'mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}')
user_preferences = pd.read_sql('SELECT * FROM Userpreference', engine)

# Transform user_preferences into a user-item matrix
user_item_matrix = user_preferences.pivot_table(index='UserID', columns='MovieID', values='Rating').fillna(0)

# Function to get genres of highly rated movies
def get_user_preferred_genres(user_id, user_movies):
    liked_movies = user_movies[user_movies['Rating'] == 1]['MovieID']
    genres = []

    for movie_id in liked_movies:
        movie_genre = movies_df[movies_df['imdbId'] == movie_id]['Genre']
        if not movie_genre.empty:
            genres.extend(movie_genre.iloc[0].split(','))  # Assuming genres are comma-separated

    return set(genres)  # Using a set to avoid duplicates


def simplified_collaborative_filtering(user_id, user_movies, num_recommendations=5):
    cosine_sim = cosine_similarity(user_item_matrix)

    try:
        user_index = user_item_matrix.index.get_loc(user_id)
    except KeyError:
        print(f"User ID {user_id} not found in user-item matrix.")
        return []

    # Get similarity scores for the target user
    sim_scores = list(enumerate(cosine_sim[user_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    recommended_movies = []
    for i, _ in sim_scores:
        if i != user_index:  # Skip the same user
            similar_user_movies = user_item_matrix.iloc[i]
            for movie_id in similar_user_movies[similar_user_movies > 0].index:
                if movie_id not in user_movies['MovieID'].values:
                    movie_title = movies_df[movies_df['imdbId'] == movie_id]['Title'].iloc[0]
                    recommended_movies.append(movie_title)
                    if len(recommended_movies) >= num_recommendations:
                        break

        if len(recommended_movies) >= num_recommendations:
            break

    if not recommended_movies:
        print("No recommendations found.")
    random.shuffle(recommended_movies)
    return recommended_movies[:num_recommendations]

# Example usage
user_id = '6575778ecc97b'  # A user id (session id is stored while the user gives rating for movies)
user_movies = user_preferences[user_preferences['UserID'] == user_id]
recommended_movies = simplified_collaborative_filtering(user_id, user_movies, 5)
print(recommended_movies)


