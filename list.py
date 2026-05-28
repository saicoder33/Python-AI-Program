# language = [ "python", "java", "c", "cpp", "javascript" ]
# print("List items :", language)

# number =[]
# for i in range(5):
#  number.append(i)

# print("List of numbers:",number)

# #user input
# name = []
# for i in range(5):
#  n=input("Enter the name:")
#  name.append(n)
# print("List of names:",name)

# #STORE EVEN NUMBERS IN  AN EMPTY LIST
# even_numbers = []
# for i in range(1,21):
#     if i % 2 == 0:
#         even_numbers.append(i)
# print("Even numbers between 1 to 20:",even_numbers)

# marks =[[12,23,30],
#         [10,50,12],
#         [45,55,78]
#         ]

# print("Marks ",marks)
# print("Marks of student 1:",marks[0][1])

# marks.insert(1,[20,30,40])
# print("Marks after inserting:",marks)

# # marks.extend()

# N=int(input("Enter the number (size of list):"))
# number=[]
# for i in range(N):
#     x=int(input("Enter a number:"))
#     number.append(x)
# print("List of numbers:",number)

# print(type(number))

#split function in list
#syntax string.split(separator,max_split)

sentence = "Hello,I'm Sai"
sentence.split(",")
print(sentence.split(",", 1))
