'''Machine Learning :It is a branch of AI ..where computer leanrs about the data and performs actions on data and we learn patterns
To learn Machine Learning we neeed some platform or library like scikit-learn.
Scikit-learn :It is used to make predictions on data.
**Some points we are going to learn**
1)Basic Mathematical concepts before learning Scikit-learn(Sk-learn)
2)Steps to learn Sk-learn

****Steps to Train a Machine Learning Model:****
     1)Load the Dataset   (From pandas)
     2)Data Cleaning      (Handling missing values, outliers etc. for data cleaning wee use dropna())
     3)Feature Selection  (Select features (X) and Target (Y) )
     4)Train-Test Split   ( Split the data into training and testing sets using train_test_split() function from sklearn.model_selection
                           Traning Data -> Used to teach the model
                           Testing Data -> Used to check performance)
     5)Choose Alogorithm   ( For predicting a numeric value , use Linear Regression.)
     6)Train the Model     ( This where actual learning happens)
     7)Prediction          ( model.predict(X_test) -> used to make predictions on the test data)
     8)Model Evaluation    ( mean_absolute_error, mean_squared_error, r2_score etc. are used to evaluate the performance of the model)
     9)Predict for new data( model.predict(new_data) -> used to make predictions on new, unseen data)

1     

'''

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error

# # # Load the dataset
# df = pd.read_csv('students.csv')

# #Display Dataset
# print("Dataset:")
# print(df)

# #Data cleaning
# df = df.dropna()  # Drop rows with missing values

# #Features (Input)
# X = df[["Hours"]]

# #Target (Output)
# Y = df["Marks"]

# #Split Data into Training and Testing Sets
# X_train , X_test , Y_train , Y_test = train_test_split(
#     X,
#     Y,
#     test_size=0.2,
#     random_state=42
# )

# #Create Linear Regression Model
# model = LinearRegression()

# #Train the Model
# model.fit(X_train,Y_train)

# #Predict on test data
# predictions = model.predict(X_test)

# #Calculate error
# error = mean_absolute_error(Y_test, predictions)
# print("Mean Absolute Error:", error)

# #new prediction
# hours = pd.DataFrame([[5]], columns=["Hours"])
# new_prediction = model.predict(hours)
# print("Predicted Marks for 5 hours of study:", new_prediction[0])

# #Display equatoin of the line
# print("Equation of the line: Y =", model.coef_[0], "* X +", model.intercept_)

'''
1)Linear regression : Preicts a continuous numeric value
    Real-life example :
    Predicting house price based on area
    formula : Y = mX + b
    where:
        Y = Predicted value (house price)
        X = Input feature (area)    
        m = slope
        b = intercept

'''
#Program based on linear regression
'''from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array ([[10001], [15000], [20000], [25000], [30000]])
Y = np.array([50, 60, 70, 80, 90])
model = LinearRegression()
model.fit(X,Y) #Use to find relation between X and Y(input and otput)

prediction = model.predict([[35000]])
print("Predicted value for 35000 is:", prediction[0])'''

'''from sklearn.linear_model import LogisticRegression
import numpy as np
salary = np.array([[30000], [40000]])
age = np.array([25, 30])
model = LogisticRegression()
model.fit(salary, age)
print("Predicted salary for age 32 is:", model.predict([[32000]]))
'''


'''
2)Logistic:Classification model 
           Predicts categories

    Real-life example:
    Will a student pass or fail based on hours of study?
    spam detectio
    disease detection

'''

from sklearn.linear_model import LogisticRegression
'''import numpy as np
X = np.array([[1], [2], [3], [4], [5]])
Y = np.array([0, 0, 0, 1, 1]) 
model = LogisticRegression()
model.fit(X, Y)
prediction = model.predict([[6]])
print("Predicted class for 6 hours of study is:", prediction[0])

'''

#customer purchase
# x = [[18],[20],[22],[40],[45],[50]]
# y = [0,0,0,1,1,1]
# model = LogisticRegression()
# model.fit(x,y)
# print(model.predict([[30]]))

'''
3)Decision Tree : Makes decisions using conditions
Real-life example:
 loan approval salary > 50000  -> approve loan
'''

# from sklearn.tree import DecisionTreeClassifier
#Loan approval based on salary and age
'''X = [
    [18, 30000],
    [20, 40000],
    [22, 50000],
    [40, 60000],
    [45, 70000],
    
]
y =['yes','yes','yes','no','no']
model = DecisionTreeClassifier()
model.fit(X,y)
print(model.predict([[30, 45000]]))
'''
#Scholarship based on marks
'''X =[[60],[70] ,[80] ,[90] ,[95]]
y = ['no','no','yes','yes','yes']
model = DecisionTreeClassifier()        
model.fit(X,y)
print(model.predict([[85]]))
'''
#Disease detection based on symptoms
'''X = [[98],[100],[102],[104],[106]]
Y = ['healthy','healthy','sick','sick','sick']
model = DecisionTreeClassifier()
model.fit(X,Y)
print(model.predict([[103]]))'''

'''
4)Random Forest: Many decision trees toghether to make a decision
Tree 1 -> yes
Tree 2 -> yes
Tree 3 -> no
More accurate than a single decision tree

'''
from sklearn.ensemble import RandomForestClassifier
'''X = [
    [25, 30000],
    [30, 40000],
    [35, 50000],
    [40, 60000],
    [45, 70000]
]
y = ['no', 'no', 'yes', 'yes', 'yes']
model = RandomForestClassifier()
model.fit(X, y)
print(model.predict([[32, 45000]]))
'''
#Insurance claim
'''X =[[4],[5],[6],[7],[8]]
y = ['no','no','yes','yes','yes']
model = RandomForestClassifier()
model.fit(X,y)
print(model.predict([[6.5]]))'''

#Fraud detection
'''X = [[100],[200],[5000],[6000]]
y = ['normal','normal','fraud','fraud']
model = RandomForestClassifier()
model.fit(X,y)
print(model.predict([[5500]]))'''

'''
5)KNN (K-Nearest Neighbors):Supervised learning algorithm used for classification and regression tasks. It works by finding the K nearest neighbors to a given data point and making predictions based on the majority class (for classification) or average value (for regression) of those neighbors.

'''

# from sklearn.neighbors import KNeighborsClassifier
# X = [[1], [2], [3], [8], [9]]
# y = [0, 0, 0, 1, 1]
# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(X, y)
# print(model.predict([[6]]))

'''
6)SVM (Support Vector Machine):Draws the best boundary between classes in the feature space. 

'''
'''from sklearn.svm import SVC
X = [[1], [2], [3], [8], [9]]
y = [0, 0, 0, 1, 1]
model = SVC()
model.fit(X, y)
print(model.predict([[6]]))
'''
