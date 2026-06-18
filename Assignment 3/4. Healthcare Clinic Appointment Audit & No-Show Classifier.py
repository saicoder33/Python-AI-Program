import pandas as pd
import numpy as np

data = {
    "Patient": ["P1", "P2", "P3", "P4"],
    "Appointment": [
        "2025-06-01 09:00",
        "2025-06-01 10:00",
        "2025-06-01 11:00",
        "2025-06-01 12:00"
    ],
    "Arrival": [
        "2025-06-01 09:05",
        "2025-06-01 10:30",
        "2025-06-01 11:00",
        "2025-06-01 12:45"
    ]
}

df = pd.DataFrame(data)

df["Appointment"] = pd.to_datetime(df["Appointment"])
df["Arrival"] = pd.to_datetime(df["Arrival"])

df["Delay"] = (
    df["Arrival"] - df["Appointment"]
).dt.total_seconds() / 60

df["Status"] = np.where(
    df["Delay"] > 20,
    "No Show Risk",
    "On Time"
)

print(df)

print("\nAverage Delay:")
print(df["Delay"].mean())