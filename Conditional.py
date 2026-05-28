age=7
a=12
b=23
if age>=18:
    print("You are an adult.")
elif a <= b:
    print("A is less than or equal to B")
    sum=a+b
    print("The sum of A and B is:",sum)
else:
    print("Wrong input")

#WAP TO CHECK WHETHER THE NUMBER IS POSITIVS,NEGATIVE AN ZERO
num=int(input("Enter a number:"))
if num>0:
    print("The number is positive.")
elif num<0:
    print("The number is negative.")
else:  
    print("The number is zero.")