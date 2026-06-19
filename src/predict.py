"""
Prediction module for AI Job Scam Detection Platform.
Loads the trained model and vectorizer and predicts
whether a job posting is Fake or Genuine.
"""

import joblib
from config import MODEL_PATH, VECTORIZER_PATH
from src.preprocessing import clean_text

# Load trained model and TF-IDF vectorizer
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


def predict_job(job_description: str) -> dict:
    """
    Predict whether a job posting is Fake or Genuine.

    Parameters
    ----------
    job_description : str
        Job description entered by the user.

    Returns
    -------
    dict
        Prediction result with probabilities.
    """

    cleaned_text = clean_text(job_description)

    features = vectorizer.transform([cleaned_text])

    prediction = model.predict(features)[0]

    probabilities = model.predict_proba(features)[0]

    return {
        "prediction": int(prediction),
        "fake_probability": round(probabilities[1] * 100, 2),
        "real_probability": round(probabilities[0] * 100, 2)
    }