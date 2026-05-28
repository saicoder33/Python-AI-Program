#Dictionary is used to store data in key-value pair
#they are unordered,mutable & dont allow duplicate keys
#syntax : dict_name = {key:value,key:value,......}

#WAP to store info 

info={
    "key":"value",
    "Name":"Sai",
    "Roll_no":33,
    "marks":[95,98,96]
    }

print(info)

info['Name']="Sai Dighe"

print(info)

info['CGPA']=9.2
print(info)

#WAP to show numbers in phone book
# phone_book={
#     "Sai":8830485678,
#     "Shrutika":9922478554,
#     "Jonny":9876543210
    
# }
# Name=input("Enter the name:")

# print("Phone number of",Name,"is",phone_book[Name])

#online shopping products

products={
    "Name":"Laptop",
    "Price":5000,
    "Brand":"Lenovo"
}

print("Product:",products["Name"])
print("Price:",products["Price"])
print("Brand:",products["Brand"])

#Nested Dictionary
student={
    "Roll_no":33,
    "Name":"Sai",
    "Marks":{
        "Cpp":95,
        "C":98,
        "Python":95
    }
}

print(student)
print(type(student))
print(student["Marks"])
print(student["Marks"]["Python"])

print(student.keys())
print(student.values())
print(student.items())
print(student.get("Name"))
print(student.update({'Name':'Sai Dighe'}))
print(student)