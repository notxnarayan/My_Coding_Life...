# ======================================================
# Soft Margin SVM - Loan Approval Example with Features
# ======================================================

import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# -----------------------------
# 1️⃣ Sample loan dataset with features
# -----------------------------
# Features:
# Interest: 'Not-Interested', 'Interested'
# Extra-Curricular-Activities: 'Good', 'Not Good'
# CreditHistory: 'Good', 'Bad'
# PropertyArea: 'Urban', 'Rural', 'Semiurban'
# LoanAmount: numeric (in $k)
# LoanTerm: numeric (months)

data = pd.DataFrame({
    'Interest': ['Not-Interested','Interested','Not-Interested','Interested','Not-Interested','Interested','Not-Interested','Interested'],
    'Extra-Curricular-Activities': ['Good','Not Good','Good','Good','Not Good','Good','Good','Not Good'],
    'Score': [100, 80, 200, 50, 150, 70, 250, 40],
    'GPA': [360, 180, 360, 120, 240, 180, 360, 120],
    'LoanStatus': [1,0,1,0,1,0,1,0]  # 1=Approved, 0=Rejected
})

X = data.drop('LoanStatus', axis=1)
y = data['LoanStatus']

# -----------------------------
# 2️⃣ Preprocess categorical features
# -----------------------------
categorical_features = ['Interest', 'Extra-Curricular-Activities']
numeric_features = ['LoanAmount', 'LoanTerm']

# ColumnTransformer to one-hot encode categorical features
preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(), categorical_features),
], remainder='passthrough')  # keep numeric features as is


# -----------------------------
# 3️⃣ Create pipeline: preprocessing + SVM
# -----------------------------
model = Pipeline([
    ('preprocess', preprocessor),
    ('svm', SVC(kernel='linear', C=1.0))
])

# -----------------------------
# 4️⃣ Train the model
# -----------------------------
model.fit(X, y)

# -----------------------------
# 5️⃣ Predict for new customer
# -----------------------------
new_customer = pd.DataFrame({
    'Interest': ['Interested'],
    'Extra-Curricular-Activities': ['Not Good'],
    'Score': [80],
    'GPA': [180]
})

prediction = model.predict(new_customer)
print("New Admission prediction:", "Approved" if prediction[0]==1 else "Rejected")