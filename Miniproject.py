import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


# 1. Load Dataset
diabetes_data = pd.read_csv("diabetes.csv")

diabetes_data = diabetes_data.dropna()
diabetes_data = diabetes_data.drop_duplicates()


# 2. Basic Data Analysis
print("Average Glucose Level:", diabetes_data["Glucose"].mean())
print("Average BMI:", diabetes_data["BMI"].mean())
print("Average Blood Pressure:", diabetes_data["BloodPressure"].mean())

print("\nDiabetes Count:")
print(diabetes_data["Outcome"].value_counts())



# 3. Data Visualization
plt.hist(diabetes_data["Glucose"], bins=20)
plt.title("Glucose Level Distribution")
plt.xlabel("Glucose")
plt.ylabel("Frequency")
plt.show()

plt.hist(diabetes_data["BMI"], bins=20)
plt.title("BMI Distribution")
plt.xlabel("BMI")
plt.ylabel("Frequency")
plt.show()

sns.histplot(diabetes_data["Glucose"], bins=20)
plt.title("Glucose Distribution using Seaborn")
plt.xlabel("Glucose")
plt.ylabel("Frequency")
plt.show()

# 4. Supervised Model
# Logistic Regression
X = diabetes_data[
    [
        "Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigreeFunction",
        "Age",
    ]
]

y = diabetes_data["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print("\nSupervised Model Accuracy:", accuracy)



# 5. Take User Input
print("\nEnter patient details:")

pregnancies = int(input("Pregnancies: "))
glucose = float(input("Glucose: "))
blood_pressure = float(input("Blood Pressure: "))
skin_thickness = float(input("Skin Thickness: "))
insulin = float(input("Insulin: "))
bmi = float(input("BMI: "))
family_history = float(input("Diabetes Pedigree Function: "))
age = int(input("Age: "))


user_data = pd.DataFrame(
    {
        "Pregnancies": [pregnancies],
        "Glucose": [glucose],
        "BloodPressure": [blood_pressure],
        "SkinThickness": [skin_thickness],
        "Insulin": [insulin],
        "BMI": [bmi],
        "DiabetesPedigreeFunction": [family_history],
        "Age": [age],
    }
)

result = model.predict(user_data)

if result[0] == 1:
    print("Prediction: Person may have diabetes risk.")
else:
    print("Prediction: Person may not have diabetes risk.")



# 6. Unsupervised Model
# KMeans Clustering
unsupervised_data = diabetes_data[
    [
        "Glucose",
        "BMI",
        "Age",
        "BloodPressure",
    ]
]

scaler = StandardScaler()
scaled_data = scaler.fit_transform(unsupervised_data)

kmeans = KMeans(n_clusters=2, random_state=42)
clusters = kmeans.fit_predict(scaled_data)

diabetes_data["Cluster"] = clusters

print("\nCluster Counts:")
print(diabetes_data["Cluster"].value_counts())

print("\nAverage values in each cluster:")
print(
    diabetes_data.groupby("Cluster")[
        [
            "Glucose",
            "BMI",
            "Age",
            "BloodPressure",
            "Outcome",
        ]
    ].mean()
)



# 7. Cluster Visualization
plt.scatter(
    diabetes_data["Glucose"],
    diabetes_data["BMI"],
    c=diabetes_data["Cluster"]
)

plt.title("KMeans Clustering: Glucose vs BMI")
plt.xlabel("Glucose")
plt.ylabel("BMI")
plt.show()