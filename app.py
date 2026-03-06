from flask import Flask, render_template, request
import numpy as np
import joblib
from graph import generate_graph

app = Flask(__name__)

# Load trained model
model = joblib.load("model/kmeans_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    income = int(request.form["income"])
    score = int(request.form["score"])

    features = np.array([[income, score]])

    cluster = model.predict(features)[0]

    cluster_info = {
    0: ("High Income Low Spenders", "Customers with high income but low spending. They have potential to spend more."),
    1: ("Low Income High Spenders", "Customers with lower income but high spending habits."),
    2: ("Average Customers", "Customers with average income and average spending behavior."),
    3: ("Very Rich Low Spenders", "Very high income customers who spend less than expected."),
    4: ("Active Shoppers", "Customers who frequently spend and are highly engaged buyers.")
}

    customer_type, description = cluster_info.get(cluster, ("Unknown", ""))

    # generate updated graph
    generate_graph(income, score)

    return render_template(
        "index.html",
        prediction=cluster,
        customer_type=customer_type,
        description=description
    )

if __name__ == "__main__":
    app.run(debug=True)