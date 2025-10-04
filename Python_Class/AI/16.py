import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Step 1: Create a User-Item Ratings Table
# -----------------------------
# Rows = Users, Columns = Movies, Values = Ratings (0 = not rated)
data = {
    'Movie1': [5,4,0,0,3],
    'Movie2': [4,0,0,3,3],
    'Movie3': [1,1,0,5,0],
    'Movie4': [0,0,5,4,0],
    'Movie5': [0,2,4,0,0]
}
ratings = pd.DataFrame(data, index=['User1','User2','User3','User4','User5'])
print("User-Item Ratings:\n", ratings)

# -----------------------------
# Step 2: Transpose for Item-Based Similarity
# -----------------------------
# Each movie becomes a vector of its ratings by all users
item_matrix = ratings.T
print(item_matrix)

# -----------------------------
# Step 3: Compute Movie-Movie Similarity
# -----------------------------
# Using cosine similarity: measures how similar movies are based on user ratings
similarity = pd.DataFrame(
    cosine_similarity(item_matrix), 
    index=item_matrix.index, 
    columns=item_matrix.index
)
print("\nMovie-Movie Similarity:\n", similarity)

# -----------------------------
# Step 4: Predict Ratings for a Target User
# -----------------------------
user = 'User3'
user_ratings = ratings.loc[user]  # Ratings of User3
print("user rating", user_ratings)
pred_ratings = {}  # Dictionary to store predicted ratings

# Loop through all movies
print("rating columnnnn",ratings.columns)
for movie in ratings.columns:
    if user_ratings[movie] == 0:  # Only predict for movies User3 hasn't rated
        # Step 4a: Find similar movies (neighbors)
        neighbors = similarity[movie].sort_values(ascending=False)  # Sort by similarity
        print("neighboursssss",neighbors)
        neighbors = neighbors.drop(movie)  # Exclude the movie itself
        print("neighboursssss111",neighbors)
        # Step 4b: Consider only neighbors that the user has already rated
        rated_neighbors = [nbr for nbr in neighbors.index if user_ratings[nbr] > 0]
        print("rated neighborssss",rated_neighbors)
        
        # Step 4c: Predict rating as average of user's ratings for rated neighbors
        if rated_neighbors:
            pred_ratings[movie] = np.mean([user_ratings[nbr] for nbr in rated_neighbors])
            print("predictedddd",pred_ratings)

# -----------------------------
# Step 5: Recommend Top Movies
# -----------------------------
# Sort predicted ratings descending to recommend movies with highest predicted score
recommendations = sorted(pred_ratings.items(), key=lambda x: x[1], reverse=True)

print("\nRecommended movies for User3:")
for movie, rating in recommendations:
    print(f"{movie} → Predicted Rating: {rating:.2f}")