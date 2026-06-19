"""
Prediction module for AI Job Scam Detection Platform.
"""

import joblib

from config import MODEL_PATH, VECTORIZER_PATH
from src.preprocessing import clean_text
from src.logger import logger


# ==========================================================
# LOAD MODEL
# ==========================================================

try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    logger.info("Model loaded successfully.")

except Exception as e:

    logger.exception(f"Unable to load model: {e}")

    raise RuntimeError(
        "Could not load the trained model."
    )


# ==========================================================
# PREDICT
# ==========================================================

def predict_job(job_description: str) -> dict:
    """
    Predict whether a job posting is Fake or Genuine.
    """

    try:

        if not job_description.strip():

            raise ValueError("Job description is empty.")

        cleaned_text = clean_text(job_description)

        logger.info("Prediction requested.")

        features = vectorizer.transform([cleaned_text])

        prediction = model.predict(features)[0]

        probabilities = model.predict_proba(features)[0]

        fake_probability = round(probabilities[1] * 100, 2)

        real_probability = round(probabilities[0] * 100, 2)

        confidence = max(fake_probability, real_probability)

        logger.info(
            f"Prediction: {'Fake' if prediction else 'Genuine'} "
            f"| Confidence: {confidence:.2f}%"
        )

        return {
            "prediction": int(prediction),
            "fake_probability": fake_probability,
            "real_probability": real_probability
        }

    except Exception as e:

        logger.exception(f"Prediction failed: {e}")

        raise