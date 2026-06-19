import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords", quiet=True)

stop_words = set(stopwords.words("english"))

def clean_text(text):

    if text is None:
        return ""

    text = text.lower()

    text = re.sub(r"[^a-zA-Z\s]", "", text)

    text = re.sub(r"\s+", " ", text).strip()

    words = [
        word
        for word in text.split()
        if word not in stop_words
    ]

    return " ".join(words)