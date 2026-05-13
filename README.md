# 🚀 Loan Approval Prediction System

A Machine Learning based web application that predicts whether a loan application will be approved or rejected based on applicant details such as income, loan amount, and credit score. The project is built using Flask and deployed online using Render.

---

# 🌟 Features

- ✅ Loan approval prediction using Machine Learning
- ✅ Random Forest Classification model
- ✅ User-friendly web interface
- ✅ Confidence score for predictions
- ✅ Login authentication system
- ✅ Dashboard with charts and analytics
- ✅ Responsive UI using Bootstrap
- ✅ Deployed online for real-time access

---

# 🧠 Technologies Used

- Python
- Flask
- Scikit-learn
- Matplotlib
- Bootstrap
- GitHub
- Render

---

# 📊 Machine Learning Model

The application uses the **Random Forest Classifier** algorithm to predict loan approval. The model is trained on applicant-related features:

- Income
- Loan Amount
- Credit Score

The trained model is saved using Pickle (`model.pkl`) and integrated with the Flask backend for real-time predictions.

---

# 🔐 Authentication System

The project includes a secure login system using Flask sessions. Only authenticated users can access the prediction dashboard and application features.

---

# 📈 Dashboard & Visualization

The dashboard displays graphical insights using Matplotlib charts, helping users understand loan approval trends and prediction distributions.

---

# 📁 Project Structure

```plaintext
loan_predictor/
│── app.py
│── model.pkl
│── requirements.txt
│── templates/
│     ├── index.html
│     ├── login.html
│     └── dashboard.html
│── static/
│     └── chart.png
