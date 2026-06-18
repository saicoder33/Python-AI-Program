import pandas as pd
import numpy as np

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Temperature": [32, np.nan, 35, 100, 34],
    "Rainfall": [10, 15, np.nan, 12, 11]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

df["Temperature"] = df["Temperature"].replace(100, np.nan)

df["Temperature"] = df["Temperature"].interpolate()
df["Rainfall"] = df["Rainfall"].interpolate()

df["Alert"] = np.where(df["Temperature"] > 40,
                       "Heat Alert",
                       "Normal")

print("\nProcessed Data:")
print(df)

print("\nAverage Temperature:", np.mean(df["Temperature"]))
print("Average Rainfall:", np.mean(df["Rainfall"]))