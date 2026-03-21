import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.ensemble import RandomForestClassifier
import pickle

data = {
    'income': [25000, 40000, 50000, 60000, 30000, 70000, 80000, 20000],
    'loan_amount': [10000, 20000, 25000, 30000, 15000, 35000, 40000, 8000],
    'credit_score': [600, 650, 700, 750, 620, 780, 800, 580],
    'approved': [0, 1, 1, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

X = df[['income', 'loan_amount', 'credit_score']]
y = df['approved']

model = RandomForestClassifier()
model.fit(X, y)

features = ['income', 'loan_amount', 'credit_score']
importance = model.feature_importances_

plt.bar(features, importance)
plt.savefig('static/importance.png')

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)