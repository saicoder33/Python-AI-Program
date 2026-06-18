import pandas as pd

data = {
    "User": ["U1", "U2", "U3", "U4"],
    "Messages": [50, 10, 40, 5],
    "Logins": [30, 8, 25, 4]
}

df = pd.DataFrame(data)

print("User Data")
print(df)

print("\nStandard Deviation of Logins:")
print(df["Logins"].std())

df["Login Change"] = df["Logins"].diff()

churn_users = df[
    (df["Messages"] < 15) &
    (df["Logins"] < 10)
]

print("\nPotential Churn Users")
print(churn_users)