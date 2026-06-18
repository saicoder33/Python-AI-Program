#Calculate the area of retangle,circle and triangle
#Area of rectangle
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# area_rectangle = length * width
# print("The area of the rectangle is: ", area_rectangle)

# #Area of circle
# radius = float(input("Enter the radius of the circle: "))
# area_circle = 3.14 * radius * radius
# print("The area of the circle is: ", area_circle)

# #Area of triangle
# base = float(input("Enter the base of the triangle: "))
# height = float(input("Enter the height of the triangle: "))
# area_triangle = 0.5 * base * height
# print("The area of the triangle is: ", area_triangle)

#Program to accept recharge amount and calculate final bill after adding 18% GST
# recharge_amount = float(input("Enter the recharge amount: "))
# gst = 0.18 * recharge_amount    
# print("GST amount: ", gst)
# final_bill = recharge_amount + gst
# print("Final bill: ", final_bill)

#Accept marks of 5 subjects and calculate total marks, percentage and grade
# marks = []
# for i in range(5):
#     mark = float(input("Enter marks for subject {}: ".format(i+1)))
#     marks.append(mark)

# total_marks = sum(marks)
# percentage = (total_marks / 500) * 100

# if percentage >= 90:
#     grade = "A+"
# elif percentage >= 80:
#     grade = "A"
# elif percentage >= 70:
#     grade = "B"
# elif percentage >= 60:
#     grade = "C"
# else:
#     grade = "D"

# print("Total marks: ", total_marks)
# print("Percentage: ", percentage)
# print("Grade: ", grade)

#Accept account balance and withdrawal amount, check if sufficient balance is available for withdrawal and print appropriate message
# account_balance = float(input("Enter your account balance: "))
# withdrawal_amount = float(input("Enter the withdrawal amount: "))
# if withdrawal_amount <= account_balance:
#     account_balance -= withdrawal_amount
#     print("Withdrawal successful. Remaining balance: ", account_balance)
# else:
#     print("Insufficient balance. Withdrawal failed.")

#Calculate electricity bill based using slab rates
# units_consumed = float(input("Enter the number of units consumed: "))
# if units_consumed <= 100:
#     bill_amount = units_consumed * 0.5
# elif units_consumed <= 200:
#     bill_amount = (100 * 0.5) + ((units_consumed - 100) * 0.75)
# elif units_consumed <= 300:
#     bill_amount = (100 * 0.5) + (100 * 0.75) + ((units_consumed - 200) * 1.20)
# else:
#     bill_amount = (100 * 0.5) + (100 * 0.75) + (100 * 1.20) + ((units_consumed - 300) * 1.50)


# print("The electricity bill amount is: ", bill_amount)

#Apply discount based on purchase amount
# purchase_amount = float(input("Enter the purchase amount: "))
# if purchase_amount >= 5000:
#     discount = 0.20 * purchase_amount
# elif purchase_amount >= 2000:
#     discount = 0.10 * purchase_amount
# else:
#     discount = 0
# final_amount = purchase_amount - discount
# print("Discount: ", discount)
# print("Final amount to be paid: ", final_amount)    
