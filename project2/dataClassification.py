# Project 2: Data Classification Using AI
# DecodeLabs - Iris Dataset Classification using K-Nearest Neighbors (KNN)

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# STEP 1: INPUT - Load and Understand the Dataset
# -------------------------------
iris = load_iris()
X = iris.data                      # Features: sepal length, sepal width, petal length, petal width
y = iris.target                    # Labels: 0=Setosa, 1=Versicolor, 2=Virginica

df = pd.DataFrame(X, columns=iris.feature_names)
df['species'] = [iris.target_names[i] for i in y]

print("First 5 rows of dataset:")
print(df.head())
print("\nDataset shape:", df.shape)
print("\nClass distribution:\n", df['species'].value_counts())
print("\nStatistical summary:\n", df.describe())

# -------------------------------
# STEP 2: PROCESS - Feature Scaling
# -------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -------------------------------
# STEP 3: PROCESS - Train-Test Split (80/20, shuffled)
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, shuffle=True
)

print("\nTraining samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

# -------------------------------
# STEP 4: PROCESS - Choosing optimal K (Elbow Method)
# -------------------------------
error_rates = []
k_range = range(1, 21)

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    pred_k = knn.predict(X_test)
    error_rates.append(np.mean(pred_k != y_test))

plt.figure(figsize=(8, 5))
plt.plot(k_range, error_rates, marker='o', linestyle='--', color='steelblue')
plt.title("Elbow Method - Choosing Optimal K")
plt.xlabel("K Value")
plt.ylabel("Error Rate")
plt.grid(True)
plt.savefig("elbow_plot.png")
plt.show()

# -------------------------------
# STEP 5: Build Final Model (K-Nearest Neighbors)
# -------------------------------
model = KNeighborsClassifier(n_neighbors=5)   # Instantiate
model.fit(X_train, y_train)                   # Fit (memorize the map)
predictions = model.predict(X_test)           # Predict (apply logic)

# -------------------------------
# STEP 6: OUTPUT - Validation
# -------------------------------
print("\n--- Confusion Matrix ---")
cm = confusion_matrix(y_test, predictions)
print(cm)

plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("confusion_matrix.png")
plt.show()

print("\n--- Classification Report ---")
print(classification_report(y_test, predictions, target_names=iris.target_names))

accuracy = accuracy_score(y_test, predictions)
f1 = f1_score(y_test, predictions, average='weighted')

print(f"\nAccuracy: {accuracy * 100:.2f}%")
print(f"F1 Score (weighted): {f1:.4f}")

# -------------------------------
# STEP 7: Test with a new/custom sample
# -------------------------------
sample = [[5.1, 3.5, 1.4, 0.2]]   # Example flower measurements
sample_scaled = scaler.transform(sample)
sample_pred = model.predict(sample_scaled)
print(f"\nPrediction for sample {sample}: {iris.target_names[sample_pred[0]]}")