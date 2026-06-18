import pandas as pd

data = {
    "Customer": ["A", "A", "B", "B", "C", "D"],
    "Spend": [500, 700, 200, 300, 1500, 2500],
    "Visits": [5, 6, 2, 3, 8, 12]
}

df = pd.DataFrame(data)

summary = df.groupby("Customer").agg({
    "Spend": "sum",
    "Visits": "sum"
})

def segment(row):
    if row["Spend"] > 2000:
        return "Premium"
    elif row["Spend"] > 1000:
        return "Gold"
    else:
        return "Regular"

summary["Category"] = summary.apply(segment, axis=1)

print(summary)