# so far we have see how to handle single
# condition and single condition with else part
# In real world you may have to handle multiple condition
# one after another, or we can call it as nested conditions

# Identify whether the given number is positive, negative 
# or zero
givennumber = 10
if (givennumber > 0):
    print("Given number is Positive")
else:
    if(givennumber == 0):
        print("Given number is Zero")
    else:
        print("Given number is Negative")

if (givennumber >= 0):
    if (givennumber == 0):
        print("Given number is Zero")
    else:
        print("Given number is Positive")
else:
    print("Given number is Negative")

if (givennumber == 0):
    print("Given number is Zero")
else:
    if (givennumber > 0):
        print("Given number is Positive")
    else:
        print("Given number is Negative")

# Let us do it using elif
if (givennumber == 0):
    print("Given number is Zero")
elif (givennumber > 0):
    print("Given number is Positive")
else:
    print("Given number is Negative")

# If you have multiple conditions buy single statement to be executed
# then we can use the shorthand if syntax
age = 27
print("Children") if (age < 10) \
    else print("Minor") if (age >= 10 and age < 18) \
    else print("Tenager") if (age >= 18 and age < 21) \
    else print("Adult") if (age >= 21 and age < 60) \
    else print("Senior")

# Using arithmetic expression in shorthand if syntax
# So far we always call print function which does not return anything
# now we want to see how to use arithmetic expression which returns value
op = "+"
x = 10
y = 5
# let us create a simple calculator using shorthand if syntax
result = x + y if (op == "+") else x - y if (op == "-") else x * y if (op == "*") else x / y

# same is applicable for function call
op = "D"
x = "Television"
result = id(x) if (op == "A") else type(x) if (op == "D") else len(x)
