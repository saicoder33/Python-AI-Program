''''Store marks of 10 students in a list and find :
a. Highest marks 
b. Lowest marks 
c. Average marks '''

# Students_marks = [85, 92, 78, 90, 88, 95, 80, 91, 87, 89]
# print("Highest Marks:", max(Students_marks))
# print("Lowest Marks:", min(Students_marks))
# print("Average Marks:", sum(Students_marks) / len(Students_marks))

'''Store attendance of students in a list and calculate attendance percentage ''' 
# Stud_attendance = [20, 18, 22, 19, 21, 17, 23, 20, 18, 22]
# total_classes = 25

# for i in range(len(Stud_attendance)):
#     percentage = (Stud_attendance[i] / total_classes) * 100
#     print("Student", i+1, ":", round(percentage, 2), "%")

''' Store grocery items in a list and allow searching for an item in the list. '''
# grocery_items =['chocolates','icecream','cookies','nutella','chips','bread','cheese']
# search_item = input("Enter the item to search: ")
# if search_item in grocery_items:
#     print(search_item, "is available in the grocery list.")
# else:
#     print(search_item, "is not available in the grocery list.")

'''Store salaries in a list and display highest , lowest and average salary'''
# emp_salaries = [50000, 60000, 55000, 70000, 65000, 80000, 75000, 90000, 85000, 95000]
# print("Highest Salary:", max(emp_salaries)) 
# print("Lowest Salary:", min(emp_salaries))
# print("Average Salary:", sum(emp_salaries) / len(emp_salaries))

'''Use a dictionary to store names and phone numbers . Search contacts '''
# phone_book={
#      "Sammy":8830485678,
#     "Sandy":9922478554,
#     "Jonny":9876543210
    
# }
# Name=input("Enter the name:")

# print("Phone number of",Name,"is",phone_book[Name])


''' ATM Management Program:
 Menu-driven program:

a. Deposit 
b. Withdraw 
c. Check Balance 
d. Exit'''

# balance = 1000
# while True:
#     print("\nATM Menu:")
#     print("a. Deposit")
#     print("b. Withdraw")
#     print("c. Check Balance")
#     print("d. Exit")
    
#     choice = input("Enter your choice: ")
    
#     if choice == 'a':
#         amount = float(input("Enter amount to deposit: "))
#         balance += amount
#         print("Amount deposited successfully.")
        
#     elif choice == 'b':
#         amount = float(input("Enter amount to withdraw: "))
#         if amount > balance:
#             print("Insufficient balance.")
#         else:
#             balance -= amount
#             print("Amount withdrawn successfully.")
            
#     elif choice == 'c':
#         print("Current Balance:", balance)
        
#     elif choice == 'd':
#         print("Thank you for using the ATM. Goodbye!")
#         break
        
#     else:
#         print("Invalid choice. Please try again.")

'''Library Management system

a. Add Book 
b. Search Book 
c. Issue Book 
d. Return Book'''

# books = {
#     "Book1": {"Title": "The Great Gatsby", "Author": "F. Scott Fitzgerald", "Available": True},
#     "Book2": {"Title": "To Kill a Mockingbird", "Author": "Harper Lee", "Available": True},
#     "Book3": {"Title": "1984", "Author": "George Orwell", "Available": True}
# }   
# while True:
#     print("\nLibrary Menu:")
#     print("a. Add Book")
#     print("b. Search Book")
#     print("c. Issue Book")
#     print("d. Return Book")
#     print("e. Exit")
    
#     choice = input("Enter your choice: ")
    
#     if choice == 'a':
#         book_id = input("Enter book ID: ")
#         title = input("Enter book title: ")
#         author = input("Enter book author: ")
#         books[book_id] = {"Title": title, "Author": author, "Available": True}
#         print("Book added successfully.")
        
#     elif choice == 'b':
#         search_title = input("Enter book title to search: ")
#         found_books = [book for book in books.values() if book["Title"].lower() == search_title.lower()]
#         if found_books:
#             for book in found_books:
#                 print(f"Title: {book['Title']}, Author: {book['Author']}, Available: {book['Available']}")
#         else:
#             print("Book not found.")
            
#     elif choice == 'c':
#         book_id = input("Enter book ID to issue: ")
#         if book_id in books and books[book_id]["Available"]:
#             books[book_id]["Available"] = False
#             print("Book issued successfully.")
#         else:
#             print("Book is not available for issue.")
            
#     elif choice == 'd':
#         book_id = input("Enter book ID to return: ")
#         if book_id in books and not books[book_id]["Available"]:
#             books[book_id]["Available"] = True
#             print("Book returned successfully.")
#         else:
#             print("Invalid book ID or the book was not issued.")
            
#     elif choice == 'e':
#         print("Thank you for using the library system. Goodbye!")
#         break
        
#     else:
#         print("Invalid choice. Please try again.")


'''Students Management System 

a. Add Student 
b. Search Student 
c. Update Marks 
d. Display All Students '''

# students = {}
# while True:
#     print("\nStudent Management Menu:")
#     print("a. Add Student")
#     print("b. Search Student")
#     print("c. Update Marks")
#     print("d. Display All Students")
#     print("e. Exit")

#     choice = input("Enter your choice: ")
#     if choice == 'a':
#         student_id = input("Enter student ID: ")
#         name = input("Enter student name: ")
#         marks = float(input("Enter student marks: "))
#         students[student_id] = {"Name": name, "Marks": marks}
#         print("Student added successfully.")

#     elif choice == 'b':
#         search_id = input("Enter student ID to search: ")
#         if search_id in students:
#             student = students[search_id]
#             print(f"ID: {search_id}, Name: {student['Name']}, Marks: {student['Marks']}")
#         else:
#             print("Student not found.")

#     elif choice == 'c':
#         student_id = input("Enter student ID to update marks: ")
#         if student_id in students:
#             new_marks = float(input("Enter new marks: "))
#             students[student_id]["Marks"] = new_marks
#             print("Marks updated successfully.")
#         else:
#             print("Student not found.")

#     elif choice == 'd':
#         if students:
#             for student_id, student in students.items():
#                 print(f"ID: {student_id}, Name: {student['Name']}, Marks: {student['Marks']}")
#         else:
#             print("No students to display.")


#     elif choice == 'e':
#         print("Thank you for using the student management system. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")

''' Restaurant Billing System 
Use:

a. Function 
b. Lists
c. Dictionary 
d. Loops '''
# menu = {
#     "Burger": 150,
#     "Pizza": 250,
#     "Pasta": 200,
#     "Salad": 100
# }
# order = []
# while True:
#     print("\nMenu:")
#     for item, price in menu.items():
#         print(f"{item}: ${price}")
    
#     choice = input("Enter the item you want to order (or 'done' to finish): ")
    
#     if choice.lower() == 'done':
#         break
#     elif choice in menu:
#         order.append(choice)
#         print(f"{choice} added to your order.")
#     else:
#         print("Item not found in the menu. Please try again.")
# if order:
#     total = sum(menu[item] for item in order)
#     print("\nYour Order:")
#     for item in order:
#         print(f"{item}: ${menu[item]}")
#     print(f"Total Bill: ${total}")
# else:
#     print("No items ordered. Thank you for visiting!")

''' Online Shopping Cart 

a. Add product 
b. Remove Product 
c. Display Cart
d. Calculate Bill '''

cart = []
while True:
    print("\nShopping Cart Menu:")
    print("a. Add Product")
    print("b. Remove Product")
    print("c. Display Cart")
    print("d. Calculate Bill")
    print("e. Exit")

    choice = input("Enter your choice: ")
    
    if choice == 'a':
        product = input("Enter product name to add: ")
        cart.append(product)
        print(f"{product} added to cart.")
        
    elif choice == 'b':
        product = input("Enter product name to remove: ")
        if product in cart:
            cart.remove(product)
            print(f"{product} removed from cart.")
        else:
            print(f"{product} not found in cart.")
            
    elif choice == 'c':
        if cart:
            print("Products in your cart:")
            for item in cart:
                print(item)
        else:
            print("Your cart is empty.")
            
    elif choice == 'd':
        if cart:
            total = len(cart) * 100  # Assuming each product costs $100
            print(f"Total Bill: ${total}")
        else:
            print("Your cart is empty. Total Bill: $0")
            
    elif choice == 'e':
        print("Thank you for shopping with us. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")

