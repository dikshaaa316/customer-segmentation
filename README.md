# Customer Segmentation (Flask Web Application)

## Overview

This project is a **machine learning powered web application** that performs **customer segmentation using the K-Means clustering algorithm**. The application is built using **Flask** and allows users to explore clustering in two ways: predicting a customer's segment using predefined features or uploading a dataset to perform clustering dynamically.

The goal of this project is to demonstrate how **unsupervised machine learning** can be integrated into a **web interface for interactive data analysis and visualization**.

---

## Key Features

### 1. Customer Segment Prediction

The application allows users to manually enter:

* **Annual Income**
* **Spending Score**

Using a **pre-trained K-Means model**, the system predicts the cluster to which the customer belongs. Along with the prediction, the app displays a **brief description of the customer type** based on spending behavior and income level.

The predicted customer point is also highlighted on a **cluster visualization graph**.

---

### 2. Preloaded Customer Dataset Clustering

The application includes a **preloaded dataset of store customers**. This dataset contains information such as income and spending score, which are used to train the clustering model.

The model divides customers into **five behavioral segments**, helping visualize patterns such as:

* High income but low spending customers
* Low income but high spending customers
* Average customers
* Highly active shoppers

This feature demonstrates how clustering helps businesses **understand different customer groups**.

---

### 3. Dataset Upload and Dynamic Clustering

Users can upload their own **CSV dataset** through the web interface.

After uploading the dataset, the application:

1. Reads the dataset using **Pandas**
2. Displays all available columns
3. Allows the user to **select any two features**
4. Runs **K-Means clustering** on the selected features
5. Generates a **cluster visualization graph**

This makes the application flexible and allows users to experiment with clustering on **custom datasets**.

---

### 4. Cluster Visualization

The system generates a **scatter plot visualization** of the clusters using **Matplotlib**.

Each cluster is represented by a **different color**, making it easy to observe how the data points are grouped. In the prediction section, the **user's input data point is highlighted** to show which cluster it belongs to.

---

## Technologies Used

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn (K-Means Clustering)

### Data Processing

* Pandas
* NumPy

### Data Visualization

* Matplotlib

### Frontend

* HTML
* CSS

---

## Project Structure

```
Customer-Segmentation/
│
├── app.py                 # Main Flask application
├── graph.py               # Graph generation logic
│
├── model/
│   └── kmeans_model.pkl   # Trained clustering model
│
├── data/
│   └── store_customers.csv
│
├── templates/
│   ├── index.html
│   ├── select_columns.html
│   └── result.html
│
├── static/
│   ├── cluster_graph.png
│   └── upload_graph.png
│
└── uploads/               # Temporary uploaded datasets
```



## How the System Works

1. The **K-Means model is trained** on customer income and spending score data.
2. Customers are grouped into **five clusters** based on their spending patterns.
3. The Flask web interface allows users to:

   * Predict a cluster for new customer inputs
   * Upload datasets and perform clustering dynamically
4. Cluster results are visualized using **scatter plots** for better understanding of data groupings.

