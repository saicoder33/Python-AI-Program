'''Matplotlib :  It is the library used for plotting the graph. 
It is used to create static, animated, and interactive visualizations in Python. 
It provides a wide range of functions for creating various types of plots, such as line plots, scatter plots, bar plots, histograms, and more. 
Matplotlib is highly customizable and allows users to control every aspect of the plot, including colors, labels, titles, and axes. It is widely used in data analysis, scientific research, 
and machine learning for visualizing data and results.'''

'''
Step 1: Python created lists
Step 2: Matplotlib created figure
Step 3: Matplotlib created axes
step 4: Matplotlib creates line object
step 5: Coordinates are plotted
step 6: Matplotlib displays the plot

Data Transformation Pipeline
Data Coordination
       |
Axes Coordinates
       |
Figure Coordinates
       |
'''



import matplotlib.pyplot as plt


# x = [1, 2, 3, 4, 5]
# y = [1, 4, 9, 16, 25]

# plt.plot(x, y)
# plt.show()

# students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
# scores = [85, 92, 78, 90, 88]

# plt.bar (students, scores)
# plt.title('Student Scores')
# plt.xlabel('Students')
# plt.ylabel('Scores')
# plt.show()

# x = ['Jan', 'Feb', 'Mar', 'Apr']
# y = [10, 20, 29, 59]

# plt.plot(x, y)
# plt.title('Sales')
# plt.xlabel('Months')
# plt.ylabel('Revenue')
# plt.show()

# months = [1,2,3,4,5]
# sales = [120,140,520,720,190]
# plt.plot(months, sales, marker='o')
# plt.title('Monthly Sales')
# plt.xlabel('Months')
# plt.ylabel('Sales')
# plt.show()

# subjects = ['Java','C','Python','JavaScript','Ruby']
# marks = [85, 90, 95, 80, 88]
# plt.bar(subjects, marks)
# plt.title("Subject Marks")
# plt.xlabel("Subjects")
# plt.ylabel("Marks")
# plt.show()

#pie chart
# expneses = [500, 300, 200, 100]
# labels = ['Rent', 'Food', 'Transportation', 'Entertainment']
# plt.pie(expneses, labels=labels)
# plt.title('Monthly Expenses')
# plt.show()

#Histogram
# marks = [85, 90, 95, 80, 88, 92, 78, 84, 91, 89]
# plt.hist(marks)
# plt.title('Marks Distribution')
# plt.xlabel('Marks')
# plt.ylabel('Frequency')
# plt.show()

#Scatter Plot
# height = [150, 160, 170, 180, 190]
# weight = [50, 60, 70, 80, 90]
# plt.scatter(height, weight)
# plt.title('Height vs Weight')
# plt.xlabel('Height (cm)')
# plt.ylabel('Weight (kg)')
# plt.show()

#Sales comparison
# months =[1,2,3,4,5]

# sales_2024 = [100,120,140,160,180]
# sales_2025=[90,130,150,170,200]

# plt.plot(months , sales_2024)
# plt.plot(months , sales_2025)
# plt.title('Sales Comparison')
# plt.show()

#Using legend
# months =[1,2,3,4,5]
# sales_2024 = [100,120,140,160,180]
# sales_2025=[90,130,150,170,200]
# plt.plot(months , sales_2024 ,label='Sales 2024')
# plt.plot(months , sales_2025,label='Sales 2025')
# plt.title('Sales Comparison')
# plt.legend() # a small box on the graph that identifies the colors of the lines
# plt.show()

# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
# sales = [100,130,150,170,190]
# plt.plot(months, sales, marker='o')
# plt.title('Monthly Sales')
# plt.xlabel('Months')
# plt.ylabel('Sales')
# plt.grid() # adds a grid to the plot, making it easier to read and interpret the data points
# plt.show()  

