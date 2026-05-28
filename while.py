count = 0
while count < 5:
    print(count)
    count += 1
print('\n')
#WAP TO PRINT NUMBERS BETWEEN 1 TO 10
num = 1
while num <= 10:
    print(num)
    num+=1
print('\n')
#WAP TO PRINT EVEN NUMBERS BETWEEN 1 TO 20
num =2
while num <= 20:
    print(num)
    num+=2

#WAP TO FIND THE SUM OF N NATURAL NUMBERS
N = int(input("Enter a number:"))
i = 1
sum = 0
while i <= N:
    sum += i
    i+=1
print('Sum',sum)

#WAP TO PRINT MULTIPLICATION TABLE
num = int(input("Enter a number to print its table:"))
i = 1
while i <=10:
    print(num,'*',i,'=',num*i)
    i+=1

#WAP TO FIND FACTORIAL OF A NUMBER
num = int(input("Enter a number to find its factorial:"))
fact = 1
i = 1
while i <= num:
    fact *= i
    i+=1
print('Factorial',fact)

#WAP TO REVERSE A NUMBER BY USING WHILE LOOP
num = int(input("Enter a number to reverse:"))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
else:
    print("Number is reversed successfully")
print('Reverse',reverse)