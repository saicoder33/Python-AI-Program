#Tuples are immutable,means we cannot change the values once we declare it
#synatx of declaring a tuple : tuple_name=(value1,value2,...)

cars = ("BMW","Ferrai","Audi","BMW")
print(type(cars))

#methods of tuple:
#1.count() - it counts the number of times a specified value appears in the tuple
#2.index() - it finds the first occurrence of a specified value and returns its index   

print(cars.index('BMW'))
print(cars.count('BMW'))

#WAP to show GPS location
location = (10.343,54.567,)
print("Latitude:",location[0])
print("Longitude:",location[1])
