import pandas as pd
import matplotlib.pyplot as plt
import joblib

def generate_graph(income=None, score=None):

    # load dataset
    data = pd.read_csv("data/store_customers.csv")

    # select features
    X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

    # remove missing values
    X = X.dropna()

    # load model
    model = joblib.load("model/kmeans_model.pkl")

    # predict clusters
    clusters = model.predict(X)

    plt.figure(figsize=(6,5))

    plt.scatter(
        X['Annual Income (k$)'],
        X['Spending Score (1-100)'],
        c=clusters,
        cmap="viridis"
    )

    # highlight user input
    if income is not None and score is not None:
        plt.scatter(income, score, color="red", s=200, label="User Input")
        plt.legend()

    plt.xlabel("Annual Income")
    plt.ylabel("Spending Score")
    plt.title("Customer Segmentation")

    # save graph
    plt.savefig("static/cluster_graph.png")

    plt.close()