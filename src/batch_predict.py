import pandas as pd
from src.predict import predict_job


def batch_predict(csv_file):
    """
    Predict Fake/Genuine for all job descriptions in a CSV file.
    The CSV must contain a column named 'description'.
    """

    # Read the CSV
    df = pd.read_csv(csv_file)

    # Check if the required column exists
    if "description" not in df.columns:
        raise ValueError(
            "CSV file must contain a column named 'description'."
        )

    predictions = []
    fake_probs = []
    genuine_probs = []

    # Predict each job description
    for text in df["description"]:

        result = predict_job(str(text))

        predictions.append(
            "Fake" if result["prediction"] == 1 else "Genuine"
        )

        fake_probs.append(result["fake_probability"])
        genuine_probs.append(result["real_probability"])

    # Add results to the dataframe
    df["Prediction"] = predictions
    df["Fake Probability (%)"] = fake_probs
    df["Genuine Probability (%)"] = genuine_probs

    return df