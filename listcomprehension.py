# We process a list and we get a new list.
# The number of list items must be same exactly with the items in the new list created
celciusvalues = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
farenheitvalues = []

for celciusvalue in celciusvalues:
    farenheitvalues.append((celciusvalue * 9/5) + 32)

print(celciusvalues)
print(farenheitvalues)

# We have prices lets us calulate the prices with sst
prices = [10, 20, 30, 40, 50, 60, 70, 80, 90]
sstprices = []
for price in prices:
    sstprices.append(price + (price * 0.06))           
print(prices)
print(sstprices)
            
# APPEND METHOD           
# append method will add the item as a last item inside the existing list
fruits = ["apple", "orange", "mango"]
newfruits = fruits # this is not creating a copy rather referring to the same location
newfruits.append("durian")
print(fruits)
print(newfruits)

fruits = ["apple", "orange", "mango"]
newfruits = []
for fruit in fruits:
    newfruits.append(fruit)
# changing newfruits will not affect the fruits
newfruits.append("rambutan")
print(fruits)
print(newfruits)

fruits = ["apple", "orange", "mango"]
newfruits = [fruit for fruit in fruits] # list comprehension
# changing newfruits will not affect the fruits
newfruits.append("grapes")
print(fruits)
print(newfruits)

celciusvalues = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
farenheitvalues = [(celciusvalue * 9/5) + 32 for celciusvalue in celciusvalues]
print(celciusvalues)
print(farenheitvalues)

# Short method, just another way instead of traditional method up there (USE THIS)
prices = [10, 20, 30, 40, 50, 60, 70, 80, 90]
sstprices = [(price + (price * 0.06)) for price in prices]
print(prices)
print(sstprices)

# LIST COMPREHENSION
# an easy to read, compact, and elegant way of creatig a list from any existing iterable object. 
# Simple way to create a new list from values in a list you already have. 
# Enclosed with [] square brackets.
fruits = ["apple", "orange", "mango"]
numberofcharacters = [len(fruit) for fruit in fruits] # list comprehension = ["Do this Output" + "for this collection" + In this situation/condition"]
print(fruits)
print(numberofcharacters)

mynumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filter the even numbers only
evennumbers = []
for mynumber in mynumbers:
    if (mynumber % 2 == 0):
        evennumbers.append(mynumber)
print(mynumbers)
print(evennumbers)

# FILTER IN LIST
# allows you to filter a range of list based on criteria you define.
mynumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evennumbers = [mynumber for mynumber in mynumbers if (mynumber % 2 == 0)]
print(mynumbers)
print(evennumbers)

mynumbers = [1,2,3,4,5,6,7,8,9]
oddnumber = [mynumber for mynumber in mynumbers if (mynumber % 2 != 0)]
print(mynumbers)
print(oddnumber)

# ITERATE FROM MULTIPLE LIST
# Created Nested For Loops. Inside the loops has if conditions.
# traditional method
shirtcolors = ["White", "Red", "Blue"]
pantcolors = ["Black", "Brown", "Blue"]
combinations = []
for shirtcolor in shirtcolors:
    for pantcolor in pantcolors:
        if (shirtcolor != pantcolor):
            combinations.append((shirtcolor, pantcolor))
print(combinations)

# Short method
combinations = [(shirtcolor, pantcolor) for shirtcolor in shirtcolors for pantcolor in pantcolors if (shirtcolor != pantcolor)]
print(combinations)

# is all the numbers in the list are even numbers ?
mynumbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
iseven = True
for mynumber in mynumbers:
    if (mynumber % 2 != 0): iseven = False
if (iseven):
    print("All items are even numbers")
else:
    print("Some items are not even numbers")

# all function takes list of boolean values
# and checks whether all the values are True
# if all are True then it returns True (and operator)
if all([(mynumber % 2 == 0) for mynumber in mynumbers]):
    print("All items are even numbers")
else:
    print("Some items are not even numbers")

# any function takes list of boolean values
# and checks whether any True is available
# if one True is there then it return True (or operator)

x = 10
y = 15
# swap the values
temp = x
x = y
y = temp
print(x, y)

x = 10
y = 15
x, y = y, x
print(x, y)

# We process a list and we get a new list
# Overhere the number of items in the original list and newly created list 
# are always same 
celciusvalues = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# using tradional for loop
farenheitvalues = []
for celciusvalue in celciusvalues:
    farenheitvalues.append((celciusvalue * 9/5) + 32)
# using list comprehension
farenheitvalues = [(celciusvalue * 9/5) + 32 for celciusvalue in celciusvalues]
# we can also solve this type of problems using map function
# map is a built in function that is an alternative to for loop
def convertCelciusToFarenheit(celciusvalue):
    return (celciusvalue * 9/5) + 32
farenheitvalues = map(convertCelciusToFarenheit, celciusvalues)
# the map function returns map object
# map object is an iterable object
# however print function do not know how to iterate the map object
# so we typecast map function to a list so that print can print the values
print(list(farenheitvalues))

# We process a list and we get a new list
# Overhere the number of items in the newly created list 
# is less than or equals to the number of items in the original list 
mynumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filter the even numbers only
evennumbers = []
for mynumber in mynumbers:
    if (mynumber % 2 == 0):
        evennumbers.append(mynumber)
# use list comprehension
evennumbers = [mynumber for mynumber in mynumbers if (mynumber % 2 == 0)]
# this type of problems can be solved using built in function called filter
# You need to create a function that returns True or False
# Function that returns True or False is also called "Predicate function"
def isEven(number):
    return number % 2 == 0
evennumbers = filter(isEven, mynumbers)
print(list(evennumbers))

# We process a list and we get a single value
# Overhere we are reducing our list to a single value
# python has many built in modules
# one such module is functools
from functools import reduce
mynumbers = [1, 2, 3, 4, 5]
# to add 2 items let us create a function
def add(previousvalue, currentvalue):
    # note the reduce function is smart
    # when we use + the previous values is initialized with 0
    # when we use * the previous values is initialized with 1
    # however you can configure the initial value for the previous value 
    return previousvalue * currentvalue
result = reduce(add, mynumbers, 2)
print("Result:", result)


listofnumbers = input("Key in numbers seperated by comma: ")
mynumbers = listofnumbers.split(",")

# Traditional method to convert list of strings to list of integers
intmynumbers = []
for mynumber in mynumbers:
    intmynumbers.append(int(mynumber))

# Convert list of strings to list of integers using list comprehension
intmynumbers = [int(mynumber) for mynumber in mynumbers]

# Convert list of strings to list of integers using map function
intmynumbers = map(int, mynumbers)

for mynumber in intmynumbers:
    print(mynumber, type(mynumber))
