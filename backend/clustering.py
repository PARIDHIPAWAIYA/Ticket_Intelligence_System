from sklearn.cluster import KMeans


def cluster_tickets(embeddings, n_clusters=10):

    model = KMeans(n_clusters=n_clusters, random_state=42)

    labels = model.fit_predict(embeddings)

    return labels, model