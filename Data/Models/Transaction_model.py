import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score, classification_report

from sklearn.ensemble import IsolationForest

df = pd.read_csv("data/transactions.csv")

print(df.head())
print(df.info())

print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())
df = df.drop_duplicates()
df["date"] = pd.to_datetime(df["date"])

print(df[df["amount"] <= 0])
df = df[df["amount"] > 0]
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["day_of_week"] = df["date"].dt.dayofweek
df["is_high_value"] = df["amount"] > 10000

def categorize_transaction(merchant):
    merchant = merchant.lower()

    if "swiggy" in merchant or "zomato" in merchant:
        return "Food"

    elif "amazon" in merchant or "flipkart" in merchant:
        return "Shopping"

    elif "uber" in merchant or "ola" in merchant:
        return "Travel"

    elif "netflix" in merchant:
        return "Entertainment"

    elif "bigbasket" in merchant:
        return "Grocery"

    elif "electricity" in merchant:
        return "Bills"

    else:
        return "Other"

df["category"] = df["merchant"].apply(categorize_transaction)


df["text"] = df["merchant"] + " " + df["description"]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df["text"])
y = df["category"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(predictions)

print(y_test)
print(predictions)



accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)

print(classification_report(y_test, predictions))




features = df[["amount"]]

iso_forest = IsolationForest(
    contamination=0.05,
    random_state=42
)

df["anomaly"] = iso_forest.fit_predict(features)


suspicious = df[df["anomaly"] == -1]

print(suspicious)


total_spending = df["amount"].sum()

print("Total Spending:", total_spending)

average_transaction = df["amount"].mean()

print("Average Transaction:", average_transaction)

maximum_transaction = df["amount"].max()

print("Highest Transaction:", maximum_transaction)

category_spending = df.groupby("category")["amount"].sum()

print(category_spending)


df["month"] = df["date"].dt.to_period("M") #cheching monthly spending

monthly_spending = df.groupby("month")["amount"].sum()

print(monthly_spending)

# creating visualizations of data

category_spending.plot(kind="bar")

plt.title("Spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=45)

plt.show()

# ploting the data into chart

monthly_spending.plot(kind="line")

plt.title("Monthly Spending")
plt.xlabel("Month")
plt.ylabel("Amount")

plt.show()

# monthly spendings

monthly_spending.plot(kind="line")

plt.title("Monthly Spending")
plt.xlabel("Month")
plt.ylabel("Amount")

plt.show()


# saving the trained model

import joblib

joblib.dump(model, "models/transaction_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

model = joblib.load("models/transaction_model.pkl")

vectorizer = joblib.load(
    "models/vectorizer.pkl"
)