import pandas as pd


DATA_PATH = "data/support_tickets.csv"


def load_tickets():

    df = pd.read_csv(DATA_PATH)

    # select useful fields
    columns = [
        "Ticket Subject",
        "Ticket Description",
        "Ticket Type",
        "Product Purchased",
        
    ]

    df = df[columns]

    # combine text fields
    df["text"] = (
        df["Ticket Subject"].fillna("") + " " +
        df["Ticket Description"].fillna("") + " " +
        df["Ticket Type"].fillna("") + " " +
        df["Product Purchased"].fillna("")
    )

    return df