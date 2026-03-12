from sklearn.feature_extraction.text import TfidfVectorizer

CUSTOM_STOPWORDS = [
    "product", "purchased", "please", "assist", "issue",
    "customer", "support", "request"
]

def generate_issue_label(texts):

    if not texts:
        return "Unknown Issue"

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=5
    )

    X = vectorizer.fit_transform(texts)

    words = vectorizer.get_feature_names_out()

    filtered = [w for w in words if w not in CUSTOM_STOPWORDS]

    if len(filtered) >= 2:
        return f"{filtered[0]} {filtered[1]}"
    elif len(filtered) == 1:
        return filtered[0]
    else:
        return "General Issue"