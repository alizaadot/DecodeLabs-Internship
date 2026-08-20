# Project 2: Data Classification Using AI
**DecodeLabs | Artificial Intelligence — Industrial Training Kit | Batch 2026**

**File:** `dataClassification.py`

---

## Goal
Build a basic classification model using a small dataset (the Iris dataset).

## Key Requirements
- Load and understand a dataset
- Split data into training and testing sets
- Apply a simple classification algorithm

## Key Skills
Data handling, supervised learning basics, model training

## Technologies Used
- Python 3
- pandas, numpy
- scikit-learn (`sklearn`)
- matplotlib, seaborn

## How It Works
- Loads the built-in **Iris dataset** (150 samples, 3 balanced classes of 50 each, 4 features)
- Applies **StandardScaler** to normalize feature values
- Splits data into training/testing sets (80/20, shuffled) using `train_test_split`
- Uses the **Elbow Method** to determine the optimal value of K
- Trains a **K-Nearest Neighbors (KNN)** classifier
- Evaluates performance using a **Confusion Matrix**, **Classification Report**, **Accuracy**, and **F1 Score**

## How to Run
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
python dataClassification.py
```

## Actual Output
```
Dataset shape: (150, 5)

Class distribution:
 species
setosa        50
versicolor    50
virginica     50

Training samples: 120
Testing samples: 30

--- Confusion Matrix ---
[[10  0  0]
 [ 0  9  0]
 [ 0  0 11]]

--- Classification Report ---
              precision    recall  f1-score   support
      setosa       1.00      1.00      1.00        10
  versicolor       1.00      1.00      1.00         9
   virginica       1.00      1.00      1.00        11
    accuracy                           1.00        30
   macro avg       1.00      1.00      1.00        30
weighted avg       1.00      1.00      1.00        30

Accuracy: 100.00%
F1 Score (weighted): 1.0000

Prediction for sample [[5.1, 3.5, 1.4, 0.2]]: setosa
```

See `elbow_plot.png` and `confusion_matrix.png` for visual outputs.

---

## Author
**Aliza**
AI 473 — Deep Learning Coursework
DecodeLabs Industrial Training Kit, Batch 2026
