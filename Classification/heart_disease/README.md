# 🫀 Heart Disease Prediction using Machine Learning

## 📌 Project Overview
This project aims to predict the presence of heart disease using machine learning techniques based on patient health and lifestyle data.
Multiple models and techniques were explored, with a strong focus on medical evaluation metrics such as recall and ROC–AUC, rather than accuracy alone.

During experimentation, it was found that model performance is fundamentally limited by the dataset, which is a key and valid data science conclusion.

## 📊 Dataset Description
The dataset contains 10,000 records with a mix of demographic, clinical, and lifestyle features.

Target Variable

Heart Disease Status

0 → No heart disease

1 → Heart disease

Feature Types

Numeric: Age, Blood Pressure, Cholesterol Level, BMI, Triglyceride Level, etc.

Binary categorical: Gender, Smoking, Diabetes, High Blood Pressure, etc.

Ordinal categorical:

Exercise Habits (Low / Medium / High)

Alcohol Consumption (Low / Medium / High)

Stress Level (Low / Medium / High)

Sugar Consumption (Low / Medium / High)

Class distribution is approximately 80% No Disease / 20% Disease.

### Target Variable
- `Heart Disease Status`
  - 0 → No Heart Disease
  - 1 → Heart Disease

### Feature Overview And data Preprocessing
The following preprocessing steps were applied:

Handling missing values using Simple Imputer

Ordinal encoding for ordered categorical variables

Binary encoding for yes/no variables

Feature scaling using StandardScaler

Stratified train–test split to preserve class distribution

Outlier analysis using box plots and MAD (Median Absolute Deviation)



## 🔍 Exploratory Data Analysis (EDA)
Summarize insights from EDA:
- Class distribution
- Correlation analysis
- Distribution plots
- Key observations

---

## 🤖 Models Used
List models that were trained:
- Logistic Regression
- Support Vector Machine

---

## 📈 Model Evaluation
Explain evaluation strategy and metrics:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- ROC–AUC

> Emphasize why recall is important for medical problems.

---

## 📉 ROC–AUC & Threshold Analysis
Describe:
- ROC curve interpretation
- AUC score
- Threshold tuning approach
- Precision–recall tra
