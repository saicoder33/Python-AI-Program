import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans

#introduction
print("Hello Master!")
print("Your One and Only Best Entertainment Platform is here !!")
print("Welcome To Netflix")

# 1.Reading the loaded dataset
data = pd.read_csv("netflix_users.csv")

# 2. Taking input columns
# Supervised Model
# Logistic Regression
X = data[["SubscriptionMonths", "WatchHours", "Logins", "Complaints"]]

# 3. Taking output column
Y = data["Churn"]

# 4.Creating and Training Model
model = LogisticRegression()
model.fit(X, Y)

# 5. User inputs for churn prediction
SubscriptionMonths = int(input("Enter the number of subscription months: "))
WatchHours = float(input("Enter the number of watch hours: "))
Logins = int(input("Enter the number of logins: "))     
Complaints = int(input("Enter the number of complaints: "))

# 6. Making prediction
new_data = pd.DataFrame([[SubscriptionMonths, WatchHours, Logins, Complaints]], columns=["SubscriptionMonths", "WatchHours", "Logins", "Complaints"])
prediction = model.predict(new_data)

print("==========Churn Prediction Result==========")

if prediction[0] == 1:
    print("The Subscriber is likely to cancel the subscription")
else:
    print("The Subscriber is likely to continue the subscription")
    
    # 7. Unsupervised Model
    print("**********KMeans Clustering**********")
    
    cluster_data = data[["WatchHours", "Logins"]]
    
    model = KMeans(n_clusters=2, random_state=0)
    model.fit(cluster_data)
    
    new_user = pd.DataFrame(
    [[WatchHours, Logins]],
    columns=["WatchHours", "Logins"])
    
    group = model.predict(new_user)
    
    if group[0] == 0:
        print("The Subscriber belongs to Cluster 0 (Less Active Users)")
    else:
        print("The Subscriber belongs to Cluster 1 (More Active Users)")