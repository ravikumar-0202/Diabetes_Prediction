# Diabetes Prediction System (For Women)

A Machine Learning-based web application that predicts the likelihood of diabetes **specifically for women**, using medical input features.

---

## Project Overview

This project uses a trained Machine Learning model to predict whether a woman is likely to have diabetes based on health parameters like glucose level, BMI, age, etc.

The application is built using **FastAPI** and provides real-time predictions through a simple web interface.

> Note: This model is trained on a dataset containing data for women only. Predictions are intended for female patients.

---

## Features

*  Diabetes prediction for women
*  FastAPI backend
*  Simple web interface
*  Real-time predictions
*  Pre-trained ML model integration

---

## Input Features

* Pregnancies
* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

---

## Tech Stack

* **Python**
* **FastAPI**
* **Scikit-learn**
* **NumPy & Pandas**
* **HTML**

---

## Machine Learning Model

* Model: Support Vector Machine(SVM)
* Files:

  * `classifier.pkl` → trained model
  * `scaler.pkl` → feature scaling

---

## How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ravikumar-0202/Diabetes_Prediction.git
cd Diabetes_Prediction
```

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
uvicorn main:app --reload
```

### 5️⃣ Open in browser

```
http://127.0.0.1:8000
```

---

## 📁 Project Structure

```
Diabetes_Prediction/
│── main.py              # FastAPI application
│── classifier.pkl      # Trained ML model
│── scaler.pkl          # Data scaler
│── index.html          # Frontend UI
│── __pycache__/        # Python cache files
```

---

## 🌐 API Endpoint

* **POST** `/predict`
* Returns:

  * `0` → No Diabetes
  * `1` → Diabetes

---

## 🌟 Future Improvements

* Deploy on cloud (Render / Vercel)
* Improve model accuracy
* Better UI/UX design
* Add input validation

---

## 🙌 Author

**Ravi Ranjan**
GitHub: https://github.com/ravikumar-0202

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
