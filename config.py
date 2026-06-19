from pathlib import Path

# Base Directory
BASE_DIR = Path(__file__).resolve().parent

# Data
DATA_DIR = BASE_DIR / "data"

RAW_DATA = DATA_DIR / "raw" / "fake_job_postings.csv"
PROCESSED_DATA = DATA_DIR / "processed" / "cleaned_jobs.csv"

# Models
MODEL_DIR = BASE_DIR / "models"

MODEL_PATH = MODEL_DIR / "job_scam_model.pkl"
VECTORIZER_PATH = MODEL_DIR / "tfidf_vectorizer.pkl"
FEATURE_COLUMNS_PATH = MODEL_DIR / "feature_columns.pkl"

# Assets
ASSETS_DIR = BASE_DIR / "assets"
CSS_FILE = ASSETS_DIR / "style.css"

# Reports
REPORT_DIR = BASE_DIR / "reports"