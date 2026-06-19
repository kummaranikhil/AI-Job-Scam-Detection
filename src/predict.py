import joblib
from pathlib import Path

from src.preprocessing import clean_text

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "models" / "job_scam_model.pkl")

tfidf = joblib.load(BASE_DIR / "models" / "tfidf_vectorizer.pkl")


def predict_job(job_description):

    cleaned = clean_text(job_description)

    features = tfidf.transform([cleaned])

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0]

    return {

        "prediction": prediction,

        "real_probability": probability[0] * 100,

        "fake_probability": probability[1] * 100

    }