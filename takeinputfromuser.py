# Python has a built in function called input
# it takes a single parameter which is the caption
# It always returns the input as string
# Let us do a greeting
yourname = input("What is your name: ")
# by default print function will print everything with space
# you can change the behaviour by adding a keyword argument
# the keyword is sep and the value is "" (empty)
# print("Hello", yourname, ", Good morning")
print("Hello ", yourname, ", Good morning", sep="")
print("Data type of the input is always string:", type(yourname))

# Let us calculate simple interest 
# interest = (principle * period * rate) / 100
principle = float(input("Enter Amount (RM): "))
period = float(input("Enter the Year: "))
rate = float(input("Enter Rate (%): "))
interest = (principle * period * rate) / 100
print("Interest amount:", interest)
print("Total amount to be paid:", principle + interest)

# How to call a function
print()
# How to pass literal as an argument to a function
print("Hello")
# How to pass variable as an argument to a function
greeting = "Hello"
print(greeting)
# How to pass arithmetic expression as an argument to a function
x = 10
y = 5
print(x + y)
# How to pass function call as an argument to a function
x = 10
print(id(x))
print(type(x))

print(greeting, "David, you are at", id(greeting), x + y)