# Algebraic Equation
# 2x + 3y = 10
# x and y are called variables
# 2, 3, 10 are called literals (values)
# I buy 10 apples. Each cost me RM1.20.
# what is the total amout to be paid?
# 10 * 1.20 = RM12.00
# quantity * price = total amount to be paid
# q * p = y <= Model

# We are creating a variable "buy" and assign 
# the string literal "Television" to the variable "buy"
buy = "Television"
# what you want to buy ?
print(buy)
buy = "Laptop"
print(buy)

quantity = 10
# here quantity is a variable assigned with a value 10
# quantity is also called Name in python
print("Quantity:", quantity)
# id is a built in function
# quantity is the argument to the built in function id
print("Address in quantity:", id(quantity))

# print("Address in quantity:", id(quantity, id(buy)))
# Note: The inner bracket is executed first
# Step 1: The function id(buy) is executed which will return 
# the address stored in the variable buy
# Step 2: Now the function id(quantity, address stored in buy) is executed
# Step 3: NoW the function print("Address in quanitity", address stored in quanity) 
# is executed

quantity = 15
print("Quantity:", quantity) # 15
print("Address in quantity:", id(quantity)) # definitely a different address
# if it returns the same address then it is not immutable object

newvalue = 15
print("Address in newvalue:", id(newvalue))
# whenever we assign a value to a variable python will scan
# and see whether the object already exists. If it exits then it will try to
# reuse the object rather than creating the object one more time.

quantity = "Fifteen"
print("Quantity:", quantity)
print("Address in quantity:", id(quantity))
print("Address in newvalue:", id(newvalue))

# Based on the data, data type is assigned to the variable
product = "Television"
quantity = 10
price = 1455.55
isAvailable = True
# to find the data type assigned to the variable we can use another built in function
# called type
print("Product:", product, "Data type:", type(product), "Address:", id(product))
print("Quantity:", quantity, "Data type:", type(quantity), "Address:", id(quantity))
print("Price:", price, "Data type:", type(price), "Address:", id(price))
print("Is Available:", isAvailable, "Data type:", type(isAvailable), "Address:", id(isAvailable))

# Let us calculate to total price to be paid
totalprice = quantity * price # statement
print("Total Price:", totalprice)

quantity = "10"
print("Quantity:", quantity, "Data type:", type(quantity), "Address:", id(quantity))
# totalprice = quantity * price
# we cannot multiply because quantity is string
# We must typecast it (convert from one data type to another data type)
# to convert string to integer we have a built in function int
totalprice = int(quantity) * price
print("Total Price:", totalprice)

price = "1455.55"
# We must typecast it (convert from one data type to another data type)
# to convert string to float we have a built in function float
totalprice = int(quantity) * float(price)
print("Total Price:", totalprice)

# ValueError we get it during typecasting
# TypeError we get it during arithmetic operation
# NameError we get when the variable is not defined/created
carplate = "JCG"
carplatenumber = 6784
# when both sides of + sign is number (int, float) python will do addition
# when both sides of the + sign is string python will do string concatenation
# We must typecast it (convert from one data type to another data type)
# to convert integer or float to string we have a built in function str
carnumber = carplate + str(carplatenumber)
print("Car Number:", carnumber)

valueone = "True"
valuetwo = 1
valuethree = 0
print(bool(valueone), type(bool(valueone)))
print(bool(valuetwo), type(bool(valuetwo)))
print(bool(valuethree), type(bool(valuethree)))
print(bool(2), type(bool(2)))
print(bool(-2), type(bool(-2)))
print(bool(-2.5), type(bool(-2.5)))
print(bool("Hello"), type(bool("Hello")))
print(bool(""), type(bool("")))
print(bool(None), type(bool(None)))

# sometimes we may want to create a variable but not assign with a value
mynonevariable = None # guy no brain
myemptyvariable = "" # guy with brain but empty
mynonevariable = 10
