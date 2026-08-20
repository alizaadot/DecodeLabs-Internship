# Project 3: AI Recommendation Logic
# DecodeLabs - Tech Stack Recommender using TF-IDF + Cosine Similarity

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------
# STEP 1: INGESTION - Build/Load the Job Role Dataset (raw_skills.csv)
# -------------------------------
# If you have your own raw_skills.csv, replace this block with:
# df = pd.read_csv("raw_skills.csv")

data = {
    "job_role": [
        "Data Scientist",
        "DevOps Engineer",
        "Backend Developer",
        "Cloud Architect",
        "Machine Learning Engineer",
        "Frontend Developer",
        "Data Analyst",
        "Systems Administrator",
        "Full Stack Developer",
        "Cybersecurity Analyst"
    ],
    "skills": [
        "Python SQL Machine Learning Data Analysis Statistics Pandas",
        "AWS Docker Kubernetes CI/CD Automation Linux Cloud",
        "Java Python SQL APIs Backend Databases REST",
        "AWS Cloud Computing Networking Security Automation Docker",
        "Python Machine Learning TensorFlow Data Structures Algorithms Neural Networks",
        "JavaScript HTML CSS React UI Frontend Web Design",
        "SQL Excel Python Data Analysis Visualization Statistics",
        "Linux Networking Automation Cloud Security Servers",
        "JavaScript Python SQL React APIs Backend Frontend",
        "Security Networking Python Cryptography Linux Cloud"
    ]
}

df = pd.DataFrame(data)
df.to_csv("raw_skills.csv", index=False)  # saves locally in PyCharm project folder
print("Job Role Dataset:")
print(df)

# -------------------------------
# STEP 2: INGESTION - Capture User Input (minimum 3 skills required)
# -------------------------------
print("\nEnter your skills (comma-separated, minimum 3 required):")
user_input = input("Example: Python, Cloud Computing, Automation\n> ")

user_skills = [skill.strip() for skill in user_input.split(",") if skill.strip() != ""]

if len(user_skills) < 3:
    raise ValueError("Please enter at least 3 skills for accurate matching.")

user_profile_text = " ".join(user_skills)
print(f"\nYour profile vector text: '{user_profile_text}'")

# -------------------------------
# STEP 3: PROCESS - Vector Mapping using TF-IDF (shared vocabulary space)
# -------------------------------
# Combine user profile + all job role skill sets into one corpus
# so they share the exact same vocabulary space
corpus = df["skills"].tolist() + [user_profile_text]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

# Separate job role vectors from the user vector
job_vectors = tfidf_matrix[:-1]      # all rows except last
user_vector = tfidf_matrix[-1]       # last row = user profile

# -------------------------------
# STEP 4: PROCESS - Scoring (Cosine Similarity)
# -------------------------------
similarity_scores = cosine_similarity(user_vector, job_vectors).flatten()
df["similarity_score"] = similarity_scores

# -------------------------------
# STEP 5: PROCESS - Sorting (descending order)
# -------------------------------
ranked_df = df.sort_values(by="similarity_score", ascending=False)

# -------------------------------
# STEP 6: OUTPUT - Filtering (Top-N list, prevent choice overload)
# -------------------------------
TOP_N = 3
top_matches = ranked_df.head(TOP_N)

print("\n" + "=" * 50)
print(f"TOP {TOP_N} RECOMMENDED CAREER PATHS")
print("=" * 50)

for rank, (_, row) in enumerate(top_matches.iterrows(), start=1):
    match_percent = row["similarity_score"] * 100
    print(f"{rank}. {row['job_role']}  —  Match: {match_percent:.1f}%")

print("\nFull ranking (all roles):")
print(ranked_df[["job_role", "similarity_score"]].to_string(index=False))