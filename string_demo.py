str1="Python is a easy language"
a=123
print("Length of string is :",len(str1))
print("Highest element in string is:",max(str1))
print("Lowest element in string is:",min(str1))
print("Sorted list of characters in string is:",sorted(str1))
print("Type of str",type(str1))
print("Type of a",type(a))
print(ord(str1[4]))
print(chr(97))

#WAP USING REPLACE FUNCTION
str2=str1.replace("easy","simple")
print("String after replacement:",str2)
print("String in lowercase:",str1.lower())
print("String in uppercase:",str1.upper())
print("String in capitalize case:",str1.capitalize())
print("Swapping:",str1.swapcase())
