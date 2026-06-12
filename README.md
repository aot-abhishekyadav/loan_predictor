# 💰 Loan Approval Predictor

## Overview

Loan Approval Predictor is a Machine Learning web application built using Flask, Scikit-learn, SQLite, HTML, CSS, and Bootstrap. The application predicts whether a loan application is likely to be approved based on the applicant's income, loan amount, and credit score.

The project also includes a complete user authentication system with registration and login functionality, prediction history storage, confidence score display, and data visualization.

---

## Features

* User Registration and Login System
* Secure Session Management
* Loan Approval Prediction using Machine Learning
* Confidence Score Display
* Risk Level Assessment
* Feature Importance 
* SQLite Database Integration
* Prediction History Storage
* Responsive Bootstrap User Interface
* Input Validation and Error Handling

---

## Technologies Used

### Backend

* Python
* Flask
* SQLite

### Machine Learning

* Scikit-learn
* Linear Regression 
* NumPy
* Pandas

### Frontend

* HTML5
* CSS3
* Bootstrap 5

### Visualization

* Matplotlib

---

## Project Structure

```text
Loan_Predictor/
│
├── app.py
├── modelpkl.py
├── model.pkl
├── database.db
│
├── templates/
│   ├── index.html
│   ├── login.html
│   └── register.html
│
├── static/
│   ├── importance.png
│   └── model_comparison.png
│
├── requirements.txt
└── README.md
```

---

## How It Works

1. User registers an account.
2. User logs into the system.
3. User enters:

   * Income
   * Loan Amount
   * Credit Score
4. The trained machine learning model processes the input.
5. The system predicts:

   * Loan Approved or Rejected
   * Confidence Score
   * Risk Level
6. Prediction details are stored in the SQLite database.

---

## Database Tables

### Users Table

| Column   | Type    |
| -------- | ------- |
| id       | Integer |
| username | Text    |
| password | Text    |

### Predictions Table

| Column       | Type    |
| ------------ | ------- |
| id           | Integer |
| income       | Integer |
| loan_amount  | Integer |
| credit_score | Integer |
| prediction   | Text    |
| confidence   | Real    |
| risk         | Text    |
| date         | Text    |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Generate Model

```bash
python modelpkl.py
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Future Improvements

* Password Hashing
* User-wise Prediction Dashboard
* PDF Report Generation
* Real Loan Dataset Integration
* Advanced Model Comparison
* Admin Panel
* Loan Analytics Dashboard

---

## Author

**Abhishek Yadav**

B.Tech Information Technology
Machine Learning Enthusiast | Aspiring Data Scientist

