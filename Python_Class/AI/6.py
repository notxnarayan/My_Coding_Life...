import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


X =np.array([[1],[2],[3],[4],[5],[6],[7]])
y=np.array([0,0,0,1,1,1,1])

model= LogisticRegression()
model.fit(X,y)

hours_new=np.array([[2.5]])
prob_pass=model.predict_proba(hours_new)[0][1]
prediction=model.predict(hours_new)[0]

print("probability of passing",prob_pass)
print("predicted class",prediction)