import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from datetime import datetime
from sklearn.model_selection import cross_val_score
import sys


def predict_stock_movement(stock_data):
    # Preprocess the data
    data = stock_data.dropna()
    data["date"] = pd.to_datetime(data["date"])
    data["date"] = data["date"].apply(lambda x: x.timestamp())
    X = data.drop(columns=["target"])
    y = data["target"]

    # Split the data into a training set and a test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train a logistic regression model on the training set
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    print(y_pred)
  

    # Evaluate the model's performance
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")

    scores = cross_val_score(model, X, y, cv=5)
    print(f"Accuracy: {scores.mean():.2f} (+/- {scores.std():.2f})")

if __name__ == "__main__":
    # Load the stock data
    stock_data = pd.read_csv("training_data.csv")

    # Predict whether the stock will go up or down
    predict_stock_movement(stock_data)
