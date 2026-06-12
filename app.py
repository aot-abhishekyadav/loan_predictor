from flask import Flask, render_template, request, redirect, session, url_for
import pickle
import numpy as np
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "loan_predictor_secret_key"

model = pickle.load(open('model.pkl', 'rb'))
MODEL_ACCURACY = 95

conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    income INTEGER,
    loan_amount INTEGER,
    credit_score INTEGER,
    prediction TEXT,
    confidence REAL,
    risk TEXT,
    date TEXT
)
''')

conn.commit()


@app.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))

    return render_template('index.html', accuracy=MODEL_ACCURACY)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            conn.commit()
            return redirect(url_for('login'))

        except:
            return render_template(
                'register.html',
                message="Username already exists "
            )

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        if user:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template(
                'login.html',
                message="Invalid username or password "
            )

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/predict', methods=['POST'])
def predict():

    if 'username' not in session:
        return redirect(url_for('login'))

    try:
        income = int(request.form['income'])
        loan = int(request.form['loan'])
        credit = int(request.form['credit'])

        if income <= 0 or loan <= 0 or credit <= 0:
            return render_template(
                'index.html',
                prediction_text="Invalid Input ",
                probability="",
                risk="",
                recommendation="Please enter valid positive values.",
                accuracy=MODEL_ACCURACY
            )

        features = np.array([[income, loan, credit]])

        prediction = model.predict(features)
        prob = model.predict_proba(features)

        confidence = round(max(prob[0]) * 100, 2)

        if prediction[0] == 1:
            result = " Loan Approved"
            recommendation = "Your financial profile looks good for loan approval."
        else:
            result = " Loan Rejected"
            recommendation = "Try reducing loan amount or improving credit score."

        if confidence >= 80:
            risk = " Low Risk"
        elif confidence >= 50:
            risk = " Medium Risk"
        else:
            risk = " High Risk"

        cursor.execute('''
        INSERT INTO predictions (
            income, loan_amount, credit_score,
            prediction, confidence, risk, date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            income,
            loan,
            credit,
            result,
            confidence,
            risk,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        conn.commit()

        return render_template(
            'index.html',
            prediction_text=result,
            probability=f"Confidence: {confidence}%",
            risk=risk,
            recommendation=recommendation,
            accuracy=MODEL_ACCURACY
        )

    except Exception as e:
        return render_template(
            'index.html',
            prediction_text="Something went wrong ",
            probability="",
            risk="",
            recommendation=str(e),
            accuracy=MODEL_ACCURACY
        )


if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))