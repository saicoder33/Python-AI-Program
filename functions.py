#Functions
#Functions are block of code that contain a specific task. 
# They are reusable and can be called multiple times in a program. 
# They can also take parameters and return values.

"""Types of function:
1)Built-in function
2)User-defined function
"""

# def add(a,b):
#     return a + b

# sum = add(10,28)
# print(sum)



# def greet_user(name):
#     message = f"Hello,{name}!"
#     print(message)

# greet_user("Sai")

# def square_number(num):
#     return num*num

# square = square_number(6)
# print("Square of a number is :", square)


# def cube(num):
#     return num*num*num

# cube_result = cube(3)
# print("Cube of a number is :", cube_result)

# def multiply(a,b):
#     return a * b        
# multiplication = multiply(5,7)
# print("Multiplication of a number is :", multiplication) 

# def result(marks):
#    if marks >= 40:
#          return "Pass"
#    else:
#             return "Fail"

# print(result(35))
# print(result(60))

#nested loops
#wap to print following pattern
'''****
   ****
   ****
   ****
   '''
# def square_pattern(rows):
#     for i in range(rows):
#         for j in range(rows):
#             print("*",end=" ")
#         print()

# print(square_pattern(4))

#Program using dictionary,function and loop
def Marks(Data):
    for student in Data:
        print("Student",student)
        for subject,mark in Data[student].items():
            print(subject,":",mark)
            
            print()

students={
    "Sai":{
        "Cpp":85,
        "C":90,
        "Python":96
    },
    "Joy":{
        "Cpp":80,
        "C":88,
        "Python":92

    },
    "Jonny":{
        "Cpp":78,
        "C":82,
        "Python":89
    }
}

print(Marks(students)) #function call