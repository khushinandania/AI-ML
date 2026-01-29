# 🧠 Customer Segmentation using Machine Learning

## 📌 Project Overview
Customer segmentation is the process of dividing customers into groups based on shared characteristics.  
This project uses **unsupervised machine learning** techniques to segment customers and uncover meaningful patterns that can help businesses improve marketing strategies and customer targeting.

---

## 🎯 Objectives
- Clean and preprocess customer data
- Handle missing values and categorical variables
- Reduce dimensionality for visualization
- Segment customers using **KMeans clustering**
- Evaluate clusters using **Elbow Method** and **Silhouette Score**
- Visualize customer segments in **2D and 3D**

---

## 🗂 Dataset Description
The dataset contains customer demographic and behavioral information:

| Column | Description |
|------|------------|
| Gender | Customer gender |
| Ever_Married | Marital status |
| Age | Age of customer |
| Graduated | Education status |
| Profession | Customer profession |
| Work_Experience | Years of work experience |
| Spending_Score | Spending behavior (Low / Average / High) |
| Family_Size | Number of family members |
| Var_1 | Categorical variable |

---

## 🧹 Data Preprocessing
Preprocessing is done using **Pipelines** and **ColumnTransformer** to avoid data leakage.

### ✔ Steps Performed
- **Missing value imputation**
  - Numeric: Median
  - Categorical: Most frequent
- **Feature scaling**
  - Numeric features scaled using `RobustScaler`
- **Encoding**
  - Ordinal Encoding for ordered categorical features
  - One-Hot Encoding for nominal features (`Profession`)
- Converted transformed data back to a pandas DataFrame

---

## 🧠 Feature Engineering
- Ordinal encoding applied to:
  - Spending_Score (Low < Average < High)
- One-Hot Encoding applied to:
  - Profession
- Numeric features scaled for distance-based clustering

---

## 📉 Dimensionality Reduction
To visualize high-dimensional data:
- **PCA (Principal Component Analysis)** was applied
- Reduced data to:
  - 3 components for 3D interactive visualization using plotly 

---

## 🔍 Clustering
### Algorithm Used
- **KMeans Clustering**

### Optimal Number of Clusters
- **Elbow Method**
- **Silhouette Score**

Based on both metrics, the optimal number of clusters chosen:
