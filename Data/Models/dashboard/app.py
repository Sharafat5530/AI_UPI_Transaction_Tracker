import streamlit as st
import pandas as pd

st.title("AI UPI Transaction Tracker")

df = pd.read_csv("data/transactions.csv")

st.subheader("Transaction Data")

st.dataframe(df)

total = df["amount"].sum()

st.metric(
    "Total Spending",
    f"₹{total:,.2f}"
)

# search bar

search = st.text_input("Search merchant")

if search:
    filtered = df[
        df["merchant"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

    st.dataframe(filtered)


# Amount filteration

minimum_amount = st.number_input(
    "Minimum Amount",
    min_value=0
)

filtered = df[df["amount"] >= minimum_amount]

st.dataframe(filtered)

