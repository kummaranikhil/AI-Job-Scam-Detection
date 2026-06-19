import joblib
import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

from src.preprocessing import clean_text

# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "raw" / "fake_job_postings.csv"

MODEL_DIR = BASE_DIR / "models"

REPORT_DIR = BASE_DIR / "reports"

MODEL_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)

# ============================================================
# LOAD DATASET
# ============================================================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv(DATA_PATH)

print(f"Dataset Shape : {df.shape}")

# ============================================================
# KEEP REQUIRED COLUMNS
# ============================================================

df = df[["description", "fraudulent"]]

df.dropna(inplace=True)

print(f"After Removing Missing Values : {df.shape}")

# ============================================================
# CLEAN TEXT
# ============================================================

print("\nCleaning Job Descriptions...")

df["description"] = df["description"].apply(clean_text)

print("Cleaning Completed!")

# ============================================================
# TF-IDF
# ============================================================

print("\nCreating TF-IDF Features...")

vectorizer = TfidfVectorizer(max_features=5000)

X = vectorizer.fit_transform(df["description"])

y = df["fraudulent"]

print(f"Feature Matrix Shape : {X.shape}")

# ============================================================
# TRAIN TEST SPLIT
# ============================================================

print("\nSplitting Dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

print(f"Training Samples : {X_train.shape[0]}")
print(f"Testing Samples  : {X_test.shape[0]}")

# ============================================================
# MACHINE LEARNING MODELS
# ============================================================

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),

    "Naive Bayes": MultinomialNB(),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),

    "Linear SVM": LinearSVC()
}

results = []

best_model = None
best_model_name = ""
best_accuracy = 0

# ============================================================
# TRAINING LOOP
# ============================================================

print("\nStarting Model Training...\n")

for name, model in models.items():

    print(f"Training {name}...")

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    precision = precision_score(y_test, predictions)

    recall = recall_score(y_test, predictions)

    f1 = f1_score(y_test, predictions)

    results.append([
        name,
        accuracy,
        precision,
        recall,
        f1
    ])

    if accuracy > best_accuracy:

        best_accuracy = accuracy

        best_model = model

        best_model_name = name

# ============================================================
# RESULTS
# ============================================================

result_df = pd.DataFrame(
    results,
    columns=[
        "Model",
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ]
)

result_df["Accuracy"] *= 100
result_df["Precision"] *= 100
result_df["Recall"] *= 100
result_df["F1 Score"] *= 100

result_df = result_df.sort_values(
    by="Accuracy",
    ascending=False
)

print("\n")
print("=" * 70)
print("MODEL COMPARISON")
print("=" * 70)

print(result_df.to_string(index=False))

print("=" * 70)
print(f"Best Model : {best_model_name}")
print(f"Accuracy   : {best_accuracy*100:.2f}%")
print("=" * 70)

# ============================================================
# SAVE MODEL
# ============================================================

print("\nSaving Best Model...")

joblib.dump(
    best_model,
    MODEL_DIR / "job_scam_model.pkl"
)

joblib.dump(
    vectorizer,
    MODEL_DIR / "tfidf_vectorizer.pkl"
)

print("Best Model Saved Successfully!")

# ============================================================
# SAVE REPORT
# ============================================================

result_df.to_csv(
    REPORT_DIR / "model_comparison.csv",
    index=False
)

print("Model Comparison Report Saved!")

print("\nProject Training Completed Successfully!")