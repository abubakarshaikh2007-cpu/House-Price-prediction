# 🏠 House Price Prediction using Linear Regression

## 📌 Project Overview
This Machine Learning project predicts house prices based on property
features such as area, number of bedrooms, and bathrooms.

The model is built using **Linear Regression** and trained on historical
housing data.

---

## 📊 Dataset Description
The dataset (`house_price.csv`) contains the following columns:

| Feature | Description |
|--------|-------------|
| area | Total house area (sq ft) |
| bedrooms | Number of bedrooms |
| bathrooms | Number of bathrooms |
| price | House price (target variable) |

---

## 🎯 Objective
To predict the **house price** for a new property using a trained
machine learning model.

---

## ⚙️ Technologies Used
- Python  
- Pandas  
- Scikit-learn  
- Machine Learning  

---

## 🧠 Machine Learning Workflow

1. Load dataset  
2. Data cleaning  
   - Remove duplicate values  
   - Handle missing values  
3. Feature selection  
4. Train–test split  
5. Model training  
6. Prediction on new house  
7. Model evaluation  

---

## 🤖 Algorithm Used
**Linear Regression**

Linear Regression finds the relationship between input features
and the target price using a best-fit straight line.

---

## 📈 Model Details

- **Weights (Coefficients)**  
  Represent the impact of each feature on house price.

- **Intercept**  
  Base price when all features are zero.

---

## 🔍 Sample Prediction

### Input
```
Area = 1600 sq ft
Bedrooms = 3
Bathrooms = 2
```

### Output
```
Predicted House Price = 72,229,972.97
```

---

## 📊 Model Evaluation

| Metric | Value |
|-------|-------|
| MAE (Mean Absolute Error) | 55,454.05 |
| R² Score | 0.9237 |

### Interpretation
- **High R² score (92%)** → Model fits data very well  
- **Low MAE** → Prediction error is small  

---

## ▶️ How to Run the Project

### 1️⃣ Install required libraries
```
pip install pandas scikit-learn
```

### 2️⃣ Run the program
```
python house_price_prediction.py
```

---

## 📁 Project Structure

```
house-price-prediction
│
├── house_price.csv
├── house_price_prediction.py
└── README.md
```

---

## ✅ Result
The trained Linear Regression model successfully predicts house prices
based on area, bedrooms, and bathrooms with strong accuracy.

---

## 👨‍💻 Author
Shaikh Abubakar

Machine Learning | Data Science
