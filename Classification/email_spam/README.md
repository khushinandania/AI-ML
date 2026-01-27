# Email Spam Classification Model

##  Project Overview
This project focuses on building a **machine learning model** that classifies emails as **Spam** or **Ham (Not Spam)** using **classification** techniques.  
The goal is to automatically detect unwanted emails and improve email filtering systems.

---

## Problem Statement
Emails contain large amounts of unstructured text data.  
Machine learning models cannot directly process text, so we:
1. Convert text into numerical features (text vectorization)
2. Train a classification model to predict whether an email is spam or ham

---

## Dataset
- The dataset contains email messages labeled as:
  - **Spam** → Unwanted or malicious emails
  - **Ham** → Legitimate emails


## ⚙️Workflow
1. **Data Loading**
2. **Text Vectorization**
 -  TF-IDF
4. **Train-Test Split**
5. **Model Training**
 - Naive Bayes / Logistic Regression 
6. **Model Evaluation**
 - Accuracy
 - Confusion Matrix
 - Precision, Recall, F1-score


## Model Used
- **Multinomial Naive Bayes** (commonly used for text classification)
- Alternative model:
- Logistic Regression