import pandas as pd

data = {
    "Transaction_ID": [101, 102, 103, 104],
    "Amount": [200, 15000, 500, 25000],
    "Hour": [14, 2, 10, 1]
}

df = pd.DataFrame(data)

fraud = df[
    (df["Amount"] > 10000) &
    ((df["Hour"] >= 23) | (df["Hour"] <= 5))
]

print("All Transactions")
print(df)

print("\nPotential Fraud Transactions")
print(fraud)