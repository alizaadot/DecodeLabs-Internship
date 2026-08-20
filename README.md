# Artificial Intelligence — Industrial Training Kit
**DecodeLabs | Batch 2026**

This repository contains three progressive AI projects completed as part of the DecodeLabs Industrial Training program. Each project builds on the previous one — moving from deterministic rule-based logic, to supervised machine learning, to similarity-based recommendation systems.

---

## 📁 Repository Structure

```
├── project1/
│   └── ruleBasedChatbot.py
├── project2/
│   ├── dataClassification.py
│   ├── elbow_plot.png
│   └── confusion_matrix.png
├── project3/
│   ├── recommendationLogic.py
│   └── raw_skills.csv
└── README.md
```

---

## 🤖 Project 1: Rule-Based AI Chatbot

**File:** `project1/ruleBasedChatbot.py`

**Goal:** Create a simple rule-based chatbot that responds to predefined user inputs using explicit control flow logic.

### Key Requirements
- Handle greetings and exit commands
- Use decision-making logic for responses
- Run in a continuous loop

### Key Skills
Control flow, decision-making logic, basic AI concepts

### Technologies Used
- Python 3 (no external libraries required)

### How It Works
- Runs inside a continuous `while` loop that keeps the chatbot active until an exit command is given
- Sanitizes user input (`.lower().strip()`) to handle inconsistent casing/whitespace
- Uses a dictionary-based knowledge base (40+ predefined intents covering greetings, small talk, AI/Python concepts, and project-related questions) with `.get()` for fast lookup and a built-in fallback response for unrecognized input
- Cleanly exits the loop using a `break` statement on exit commands (`bye`, `exit`, `quit`, `goodbye`)

### How to Run
```bash
python ruleBasedChatbot.py
```

### Sample Output
```
============================================================
RULE-BASED AI CHATBOT
============================================================
Hello! I am RuleBot, your simple AI chatbot.
You can ask me about AI, Python, chatbots, or this project.
Type 'bye', 'exit', or 'quit' whenever you want to leave.
============================================================

You: hi
Bot: Hello! How can I help you?

You: what is ai
Bot: AI stands for Artificial Intelligence. It is the field of creating systems that can perform tasks that normally require human intelligence.

You: bye
Bot: Goodbye! Have a great day.

Thank you for using RuleBot!
```

---

## 🌸 Project 2: Data Classification Using AI

**File:** `project2/dataClassification.py`

**Goal:** Build a basic classification model using a small dataset (the Iris dataset).

### Key Requirements
- Load and understand a dataset
- Split data into training and testing sets
- Apply a simple classification algorithm

### Key Skills
Data handling, supervised learning basics, model training

### Technologies Used
- Python 3
- pandas, numpy
- scikit-learn (`sklearn`)
- matplotlib, seaborn

### How It Works
- Loads the built-in **Iris dataset** (150 samples, 3 balanced classes of 50 each, 4 features)
- Applies **StandardScaler** to normalize feature values
- Splits data into training/testing sets (80/20, shuffled) using `train_test_split`
- Uses the **Elbow Method** to determine the optimal value of K
- Trains a **K-Nearest Neighbors (KNN)** classifier
- Evaluates performance using a **Confusion Matrix**, **Classification Report**, **Accuracy**, and **F1 Score**

### How to Run
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
python dataClassification.py
```

### Actual Output
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

## 🎯 Project 3: AI Recommendation Logic

**File:** `project3/recommendationLogic.py`

**Goal:** Create a simple recommendation system based on user preferences — a **Tech Stack Recommender** that maps a user's skills to suitable job roles.

### Key Requirements
- Take user input (choices or interests) — minimum 3 skills
- Match preferences using similarity logic
- Display recommended items (Top 3 ranked matches)

### Key Skills
Logic building, pattern matching, recommendation concepts

### Technologies Used
- Python 3
- pandas
- scikit-learn (`TfidfVectorizer`, `cosine_similarity`)

### How It Works
- Uses **Content-Based Filtering** (not collaborative filtering) — no historical user data required
- Builds/loads a `raw_skills.csv` dataset mapping 10 job roles to their associated skills
- Converts user input and job role skill sets into a shared vocabulary space using **TF-IDF** vectorization
- Calculates **Cosine Similarity** between the user's profile vector and each job role's vector
- Follows a 4-step pipeline: **Ingestion → Scoring → Sorting → Filtering**
- Outputs the **Top 3** most relevant career matches with percentage scores

### How to Run
```bash
pip install pandas scikit-learn
python recommendationLogic.py
```
When prompted, enter at least 3 skills separated by commas.

### Actual Output
```
Enter your skills (comma-separated, minimum 3 required):
> data analyst, Data Scientist, Frontend Developer

==================================================
TOP 3 RECOMMENDED CAREER PATHS
==================================================
1. Data Analyst  —  Match: 18.0%
2. Data Scientist  —  Match: 17.2%
3. Machine Learning Engineer  —  Match: 14.5%

Full ranking (all roles):
                 job_role  similarity_score
             Data Analyst          0.180278
           Data Scientist          0.171981
Machine Learning Engineer          0.144989
     Full Stack Developer          0.118382
       Frontend Developer          0.091991
          DevOps Engineer          0.000000
        Backend Developer          0.000000
          Cloud Architect          0.000000
    Systems Administrator          0.000000
    Cybersecurity Analyst          0.000000
```

---

## 👤 Author

**Aliza**
AI 473 — Deep Learning Coursework
DecodeLabs Industrial Training Kit, Batch 2026

---

## 📄 License

This repository is for educational purposes as part of the DecodeLabs Industrial Training Program.
