from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

# Step 1: Dataset
resumes = [
    "Experience in Python, Django, and REST APIs",
    "Familiar with cooking and sales, no programming",
    "Worked with Java, Spring Boot, and SQL databases",
    "Experienced in marketing and communication",
    "Skilled in machine learning, Python, and Pandas",
    "Knowledge of sales, customer service"
]
labels = [1,0,1,0,1,0]

# Step 2: Convert text to features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(resumes)

# Step 3: Train SVC
model = SVC(kernel='linear')
model.fit(X, labels)

# Step 4: Predict new resume
# new_resume = ["Chief technology officers (CTOs) shape both what a company makes and the culture in which it's made."]
new_resume = ["No Experiance"]
new_X = vectorizer.transform(new_resume)
prediction = model.predict(new_X)

print("Prediction:", "Qualified" if prediction[0]==1 else "Not Qualified")