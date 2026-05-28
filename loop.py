# language='Python'
# for i in language:
#     print(i)

# #WAP to print numbers from 1 to 5
# for i in range(1,6,2):
#     print(i)

#WAP TO PRINT EVEN NUMBERS 
for i in range(2,11,2):
    print(i)

print('\n')
#WAP TO PRINT ODD NUMBERS
for i in range(1,11,2):
    print(i)

print('\n')
#WAP SUM OF NUMBERS BETWEEN 1 TO 5
sum=0
for i in range(1,6):
    sum=sum+i
print('Sum',sum)

#WAP TO PRINT MULTIPLICATION TABLE
num=4
for i in range(1,11):
    print(num,'*',i,'=',num*i)

#WAP TO PRINT FACTORIAL OF A NUMBER
num=int(input("Enter a number:"))
fact=1
for i in range(1, num+1):
    fact=fact*i
print('Factorial',fact)



