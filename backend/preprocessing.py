import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

STOPWORDS = set(stopwords.words("english"))


def clean_text(text):

    text = text.lower()

    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"\S+@\S+", " ", text)
    text = re.sub(r"[^a-z\s]", " ", text)

    words = text.split()

    words = [w for w in words if w not in STOPWORDS]

    return " ".join(words)


def preprocess_dataframe(df):

    df["clean_text"] = df["text"].apply(clean_text)

    return df