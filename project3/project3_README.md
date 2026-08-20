# Project 3: AI Recommendation Logic
**DecodeLabs | Artificial Intelligence — Industrial Training Kit | Batch 2026**

**File:** `recommendationLogic.py`

---

## Goal
Create a simple recommendation system based on user preferences — a **Tech Stack Recommender** that maps a user's skills to suitable job roles.

## Key Requirements
- Take user input (choices or interests) — minimum 3 skills
- Match preferences using similarity logic
- Display recommended items (Top 3 ranked matches)

## Key Skills
Logic building, pattern matching, recommendation concepts

## Technologies Used
- Python 3
- pandas
- scikit-learn (`TfidfVectorizer`, `cosine_similarity`)

## How It Works
- Uses **Content-Based Filtering** (not collaborative filtering) — no historical user data required
- Builds/loads a `raw_skills.csv` dataset mapping 10 job roles to their associated skills
- Converts user input and job role skill sets into a shared vocabulary space using **TF-IDF** vectorization
- Calculates **Cosine Similarity** between the user's profile vector and each job role's vector
- Follows a 4-step pipeline: **Ingestion → Scoring → Sorting → Filtering**
- Outputs the **Top 3** most relevant career matches with percentage scores

## How to Run
```bash
pip install pandas scikit-learn
python recommendationLogic.py
```
When prompted, enter at least 3 skills separated by commas.

## Actual Output
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

## Author
**Aliza**
AI 473 — Deep Learning Coursework
DecodeLabs Industrial Training Kit, Batch 2026
