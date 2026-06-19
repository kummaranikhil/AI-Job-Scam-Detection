"""
Text preprocessing module for AI Job Scam Detection Platform.
"""

import re


def clean_text(text: str) -> str:
    """
    Clean and normalize job description text.

    Parameters
    ----------
    text : str
        Raw job description.

    Returns
    -------
    str
        Cleaned text.
    """

    if not isinstance(text, str):
        return ""

    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Remove email addresses
    text = re.sub(r"\S+@\S+", " ", text)

    # Remove numbers
    text = re.sub(r"\d+", " ", text)

    # Remove punctuation
    text = re.sub(r"[^\w\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text