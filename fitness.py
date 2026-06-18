import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_csv("fitness_data.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

print("Fitness Data:")
print(df)

# Basic analysis
print("\nAverage Steps:", np.mean(df["Steps"]))
print("Average Calories:", np.mean(df["Calories"]))
print("Average Sleep Hours:", np.mean(df["SleepHours"]))
print("Maximum Steps:", df["Steps"].max())
print("Minimum Steps:", df["Steps"].min())

# Machine Learning: Predict Calories
X = df[["Steps", "HeartRate", "SleepHours", "WorkoutMinutes"]]
y = df["Calories"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

error = mean_absolute_error(y_test, predictions)
print("\nModel Error:", error)

# Graph 1: Steps per day
plt.figure()
plt.plot(df["Date"], df["Steps"], marker="o")
plt.title("Daily Steps")
plt.xlabel("Date")
plt.ylabel("Steps")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Graph 2: Calories burned per day
plt.figure()
plt.bar(df["Date"], df["Calories"])
plt.title("Daily Calories Burned")
plt.xlabel("Date")
plt.ylabel("Calories")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Graph 3: Sleep Hours
plt.figure()
plt.plot(df["Date"], df["SleepHours"], marker="o")
plt.title("Sleep Hours")
plt.xlabel("Date")
plt.ylabel("Hours")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


user_step = int(input("Enter your steps for today:"))
user_heart_rate = int(input("Enter your average heart rate for today:"))
user_sleep_hours = float(input("Enter your sleep hours for last night:"))
user_workout_minutes = int(input("Enter your workout minutes for today:"))

# Predict calories for new input
new_data = pd.DataFrame({
    "Steps": [user_step],
    "HeartRate": [user_heart_rate],
    "SleepHours": [user_sleep_hours],
    "WorkoutMinutes": [user_workout_minutes]
})

predicted_calories = model.predict(new_data)
print("Predicted Calories Burned:", round(predicted_calories[0], 2))
plt.plot(user_step, predicted_calories, marker="o", color="red")