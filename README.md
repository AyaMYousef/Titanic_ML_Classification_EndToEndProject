# Titanic ML Classification – End-to-End Project 🚢

## 📌 Overview

This project implements an **end-to-end machine learning pipeline** to predict whether a passenger survived the Titanic disaster based on various features.
It includes **data preprocessing**, **feature engineering**, **model training**, **evaluation**, and **API deployment** for real-time predictions.

---

## 🛠 Features

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA) with visualizations
* Feature engineering (family size, is\_child, is\_alone, etc.)
* Model training using various ML algorithms
* Model evaluation with multiple metrics
* FastAPI backend for predictions
* Docker support for containerized deployment

---

## 📂 Project Structure

```
.
├── data/                # Raw and processed datasets
├── notebooks/           # Jupyter notebooks for EDA and experiments
├── src/                 # Source code
│   ├── preprocessing/   # Data preprocessing scripts
│   ├── features/        # Feature engineering scripts
│   ├── models/          # Training and evaluation
│   ├── api/             # FastAPI application
│   └── utils/           # Helper functions
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker build configuration
└── README.md            # Project documentation
```

---

## 📊 Dataset

The dataset is from the [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic), containing passenger details such as:

* Passenger ID
* Age
* Sex
* Fare
* Embarked Port
* SibSp (siblings/spouses aboard)
* Parch (parents/children aboard)
* Pclass (ticket class)

---

## 🚀 Installation & Usage

### 1️⃣ Clone the repository

```bash
git clone https://github.com/AyaMYousef/Titanic_ML_Classification_EndToEndProject.git
cd Titanic_ML_Classification_EndToEndProject
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the FastAPI app

```bash
uvicorn src.api.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000/docs
```

---

## 📦 API Endpoints

### **`POST /predict`** – Make a prediction

**Request JSON**:

```json

{
  "passenger_id": 1,
  "age": 29.0,
  "fare": 72.5,
  "sex": "female",
  "embarked": "S",
  "parch": 0,
  "sibsp": 1,
  "pclass": 1
}
```

**Response JSON**:

```json
{
  "prediction": "survived"
}
```

---
**Model Performance**:
<img width="1165" height="547" alt="image" src="https://github.com/user-attachments/assets/f45708f8-8385-4f13-97da-2569c7836957" />





