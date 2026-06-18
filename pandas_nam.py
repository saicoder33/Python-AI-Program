import pandas as pd

# Create a dictionary
student = {
    "Name": ["Namrata", "Rahul", "Priya"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 88]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(student)

# Display DataFrame
print("Student Data:")
print(df)
