import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# User-Product Ratings
data = {
    'Laptop': [5,4,0,3,0],
    'Mouse': [4,0,0,3,2],
    'Keyboard': [0,0,5,0,4],
    'Headphones': [0,5,4,0,0],
    'Monitor': [0,3,0,5,0]
}
ratings = pd.DataFrame(data, index=['User1','User2','User3','User4','User5'])

# -----------------------------
# Step 1: Compute product-product similarity
# -----------------------------
item_matrix = ratings.T
similarity = pd.DataFrame(cosine_similarity(item_matrix), index=item_matrix.index, columns=item_matrix.index)

# -----------------------------
# Step 2: Predict ratings for User1
# -----------------------------
target_user = 'User1'
user_ratings = ratings.loc[target_user]
pred_ratings = {}

for product in ratings.columns:
    if user_ratings[product] == 0:
        neighbors = similarity[product].sort_values(ascending=False).drop(product)
        rated_neighbors = [nbr for nbr in neighbors.index if user_ratings[nbr] > 0]
        if rated_neighbors:
            pred_ratings[product] = sum([user_ratings[nbr] for nbr in rated_neighbors]) / len(rated_neighbors)

# -----------------------------
# Step 3: Recommend top products
# -----------------------------
recommendations = sorted(pred_ratings.items(), key=lambda x: x[1], reverse=True)
print("Recommended products for User1:")
for product, rating in recommendations:
    print(f"{product} → Predicted Rating: {rating:.2f}")