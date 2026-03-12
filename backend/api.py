from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.ingestion import load_tickets
from backend.preprocessing import preprocess_dataframe
from backend.embeddings import generate_embeddings
from backend.clustering import cluster_tickets
from backend.trend_detection import detect_trends
from backend.issue_labeler import generate_issue_label
from backend.classification import train_classifier

app = FastAPI()



cached_results = None
cached_trends = None
cached_model = None



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/issues")
def get_issues():

    global cached_results
    global cached_model

    if cached_results is not None:
        return cached_results

    # Load dataset
    df = load_tickets()

    # Clean text
    df = preprocess_dataframe(df)

    # Generate embeddings
    embeddings = generate_embeddings(df["clean_text"].tolist())

    # -----------------------------
    # CLASSIFICATION
    # -----------------------------

    labels = df["Ticket Type"]

    if cached_model is None:
        cached_model = train_classifier(embeddings, labels)

    df["predicted_type"] = cached_model.predict(embeddings)

    # -----------------------------
    # CLUSTERING
    # -----------------------------

    cluster_labels, _ = cluster_tickets(embeddings)

    df["cluster"] = cluster_labels

    # Count tickets per cluster
    clusters = df.groupby("cluster").size().reset_index(name="mentions")

    results = []

    for _, row in clusters.iterrows():

        cluster_id = int(row["cluster"])

        cluster_df = df[df["cluster"] == cluster_id]

        cluster_texts = cluster_df["clean_text"].tolist()

        # Issue label
        issue_name = generate_issue_label(cluster_texts)

        # Most common predicted category
        category = cluster_df["predicted_type"].mode()[0]

        # Example tickets
        examples = cluster_texts[:3]

        results.append({
            "cluster": cluster_id,
            "issue": issue_name,
            "category": category,
            "mentions": int(row["mentions"]),
            "examples": examples
        })

    cached_results = results

    return results


# -----------------------------
# TRENDS API
# -----------------------------

@app.get("/trends")
def get_trends():

    global cached_trends

    if cached_trends is not None:
        return cached_trends

    df = load_tickets()

    df = preprocess_dataframe(df)

    embeddings = generate_embeddings(df["clean_text"].tolist())

    cluster_labels, _ = cluster_tickets(embeddings)

    df["cluster"] = cluster_labels

    trends = detect_trends(df)

    cached_trends = trends

    return trends