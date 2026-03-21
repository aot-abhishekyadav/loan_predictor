from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    income = int(request.form['income'])
    loan = int(request.form['loan'])
    credit = int(request.form['credit'])

    # ✅ INPUT VALIDATION HERE
    if income <= 0 or loan <= 0 or credit <= 0:
        return render_template('index.html',
               prediction_text="Invalid Input ❌",
               probability="")

    features = np.array([[income, loan, credit]])

    prediction = model.predict(features)
    prob = model.predict_proba(features)

    confidence = round(max(prob[0]) * 100, 2)

    if prediction[0] == 1:
        result = "✅ Loan Approved"
    else:
        result = "❌ Loan Rejected"

    return render_template('index.html',
                           prediction_text=result,
                           probability=f"Confidence: {confidence}%")

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))