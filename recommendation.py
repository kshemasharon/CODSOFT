import numpy as np

# Sample user-item ratings matrix (rows: users, columns: movies)
# 0 indicates no rating given
ratings = np.array([[4, 5, 0, 0, 1],
                    [0, 2, 3, 4, 5],
                    [1, 0, 0, 5, 4],
                    [5, 4, 3, 0, 0]])

# Function to compute similarity between two users (Cosine Similarity)
def similarity(user1, user2):
    mask = np.logical_and(user1 != 0, user2 != 0)
    if np.sum(mask) == 0:
        return 0
    return np.dot(user1[mask], user2[mask]) / (np.linalg.norm(user1[mask]) * np.linalg.norm(user2[mask]))

# Function to generate movie recommendations for a user
def recommend(user_id, ratings, similarity):
    user_ratings = ratings[user_id]
    similar_users = [(similarity(user_ratings, ratings[i]), i) for i in range(ratings.shape[0]) if i != user_id]
    similar_users.sort(reverse=True)  # Sort by similarity in descending order

    recommended_movies = set()
    for _, user in similar_users[:2]:  # Consider top 2 similar users
        recommended_movies.update(np.where(ratings[user] == 0)[0])

    return recommended_movies

# Example usage
user_id = 0
recommended_movies = recommend(user_id, ratings, similarity)

print(f"Recommended movies for user {user_id}:")
for movie_id in recommended_movies:
    print(f"Movie {movie_id}")

