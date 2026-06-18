import pandas as pd
import numpy as np

employees = pd.DataFrame({
    "Employee": ["A", "B", "C", "D"],
    "Salary": [30000, 45000, 50000, 60000],
    "Performance": [2, 4, 5, 3]
})

conditions = [
    employees["Performance"] >= 5,
    employees["Performance"] >= 4,
    employees["Performance"] >= 3
]

choices = [0.20, 0.15, 0.10]

employees["Hike %"] = np.select(conditions, choices, default=0.05)

employees["New Salary"] = employees["Salary"] + (
    employees["Salary"] * employees["Hike %"]
)

employees = employees.sort_values(
    by="New Salary",
    ascending=False
)

print(employees)