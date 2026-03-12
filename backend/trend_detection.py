import pandas as pd


def detect_trends(df):

    results = []

    midpoint = len(df) // 2

    first_half = df.iloc[:midpoint]
    second_half = df.iloc[midpoint:]

    clusters = df["cluster"].unique()

    for c in clusters:

        prev = len(first_half[first_half["cluster"] == c])
        curr = len(second_half[second_half["cluster"] == c])

        if curr > prev:
            trend = "Increasing"
        elif curr < prev:
            trend = "Decreasing"
        else:
            trend = "Stable"

        results.append({
            "cluster": int(c),
            "previous": int(prev),
            "current": int(curr),
            "trend": trend
        })

    return results