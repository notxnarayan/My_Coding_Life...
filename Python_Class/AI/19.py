# ======================================================
# Linear SVM - Spam Email Filter with Real Email Text
# ======================================================

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
import numpy as np

# -----------------------------
# 1. Sample email dataset
# -----------------------------
emails = [
    "Hey, let's meet tomorrow for lunch",        # Not Spam
    "Free money! Click here to claim your prize", # Spam
    "Your account has been updated",             # Not Spam
    "Win a brand new car now! Limited offer!",   # Spam
    "Are you coming to the meeting?",            # Not Spam
    "Congratulations! You won a lottery!",      # Spam
]

# Labels: 0 = Not Spam, 1 = Spam
y = np.array([0,1,0,1,0,1])

# -----------------------------
# 2. Convert text to numerical features
# -----------------------------
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)  # Converts text to bag-of-words vector
print(X)

# -----------------------------
# 3. Train Linear SVM
# -----------------------------
model = SVC(kernel='linear', C=1.0)
model.fit(X, y)

# -----------------------------
# 4. Predict new email
# -----------------------------
new_email = ["Can you free up your schedule?"]  # New email text
X_new = vectorizer.transform(new_email)
print(X_new)
prediction = model.predict(X_new)

print("Prediction for new email:", "Spam" if prediction[0]==1 else "Not Spam")