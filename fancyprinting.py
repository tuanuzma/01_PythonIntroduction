product = "Television"
quantity = 10 
price = 1455.55
isAvailable = True

# % operator is also overloaded such as +, -, *, /
# it is used for substituting values
# %s is string substitute. %d is integer substitute. %f is float substitute. %.2f is float substitute with 2 decimal places
result = "I bought %s today. Total number: %d, Per Price: %f" % (product, quantity, price)
print(result)

result = "I bought %20s today. Total number: %d, Per Price: %.2f" % (product, quantity, price)
print(result)

# Formatted strings are also called f-strings

# First method
result = f"{product:20s}{quantity:5d}{price:10.2f}"
print(result)

# Second method
print("=" * 35)
result = f"{product:20s}{quantity:5d}{price:10.2f}"
print(result)
print("=" * 35)

# Third method (allign)
print("=" * 35)
result = f"{product:20s}{quantity:5d}{price:10.2f}"
print(result)
print(f"{product:>20s}{quantity:<5d}{price:^10.2f}")
print(f"{product:>20s}{quantity:<5}{price:^10.2f}")
print("=" * 35)

# Is all the numbers in the list are even numbers ?
mynumbers = [2, 4, 6, 8, 10, 12, 14, 16, 18,20]
iseven = True
for mynumber in mynumbers:
    if (mynumber % 2 != 0):  iseven = False
if(iseven):
    print("All items are even numbers")
else:
    print("Some items are note even numbers")


# all function takes list of boolean values
# and checks whether all the values are True
# if all are True

x = 10
y = 15
# swapping two variables

# First method
temp = x 
x = y
y = temp
print(x,y)

# Second method
x = 10
y = 15
x,y = y,x
print(x,y)
