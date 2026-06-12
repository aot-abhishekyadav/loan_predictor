import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import os

# Create static folder
os.makedirs("static", exist_ok=True)

# Dataset
data = {
    'income': [25000, 40000, 50000, 60000, 30000, 70000, 80000, 20000],
    'loan_amount': [10000, 20000, 25000, 30000, 15000, 35000, 40000, 8000],
    'credit_score': [600, 650, 700, 750, 620, 780, 800, 580],
    'approved': [0, 1, 1, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

# Features & Labels
X = df[['income', 'loan_amount', 'credit_score']]
y = df['approved']

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Model
model = LinearRegression()

# Train
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Convert regression output into class 0 or 1
predicted_classes = [1 if p >= 0.5 else 0 for p in predictions]

# Accuracy
accuracy = accuracy_score(y_test, predicted_classes)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Model Accuracy Comparison Graph
models = ['Linear Regression']
accuracies = [accuracy * 100]

plt.figure(figsize=(6, 4))
plt.bar(models, accuracies)
plt.title("Model Accuracy Comparison")
plt.xlabel("Model")
plt.ylabel("Accuracy (%)")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig('static/model_comparison.png')
plt.close()

# Save Model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model Saved Successfully ")