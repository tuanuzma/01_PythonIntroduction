# Is given number is positive ?
x = 10

# if (true): execute statement
if (x >= 0): print("Given Number is Positive")

# The above syntax is suitable only if we have
# single statement to be executed
# But if you have more than 1 statement to be executed when the condition is True
# then we have to create a "code block" (paragraph of statements)
if (x > 0):
    # the code inside this block gets executed conditionally
    print("Given number is:", x)
    print("Given number is Positive")

# Is the given number even or odd ??
x = 7
if (x % 2 == 0):
    # this code gets executed only when the condition returns True
    print("Given Number is:", x)
    print("Given Number is Even")
else:
    # this code gets executed only when the condition returns False
    print("Given Number is: ", x)
    print("Given Number is Odd")

# What if I have only one statement to be executed for True 
# and only one statement to be executed for False
print("Even") if (x % 2 == 0) else print("Odd")

if (x % 2 == 0): 
    print("Even") 
else:
    print("Odd")


age = 10
# let us find whether the age is in a range
if (age >= 21 and age <= 60):
    print("You are eligible to attend this program")
else:
    print("You are not eligible to apply")
