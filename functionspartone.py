# USER DEFINED FUNCTIONS(PROGRAMMER)

# Let us create our own function
# The objective of the function is whenever it gets called
# it will print Hello World
# To create a function we use the keyword def
# followed by the function name
# Again which is followed by ()
# Which then followed by "block of code"

def sayHelloWorld():
    print("Hello World")  # this line function are purely to rechange and control all in one code.

# how to call/invoke a function
# functionname followed by ()
sayHelloWorld()

# FUNCTION DEFINITION
def greeting(name):
    # since there is one argument required
    # for this function, we must declare 1 parameter
    print("Good Morning" + str(name));

# FUNCTION CALLER
greeting("David") # David is the argument
# Note: Number of arguments must match the number of parameters
greeting("Peter")

def simpleInterest(principle, period, rate):
    interest = (principle * period * rate) / 100
    print(interest)

# the caller has access to principle, period and rate
# however no way for the caller to know the interest amount
simpleInterest(1000, 1, 6)
simpleInterest(1000, 2, 5)

# PASSED KEYWORD ARGUMENTS
# the simpleInterest is not returning any value
# which means if you try to print the value it will print None
print(simpleInterest(1000, 2, 5)) # None

# RETURN VALUE FROM FUNCTIONS
def calculateSimpleInterest(principle, period, rate):
    interest = (principle * period * rate) / 100
    return interest

print("Interest Amount: ", calculateSimpleInterest(1000, 1, 6))
print("Interest Amount: ", calculateSimpleInterest(1000, 3, 5))
interestAmount = calculateSimpleInterest(2000, 1, 6)
print("Principle Amount:", 2000)
print("Year:", 1)
print("Rate:", 6)
print("Interest Amount:", interestAmount)

# WRITE FUNCTION IN OTHER PROGRAMME AND IMPORT TO ANOTHER PROGRAMME
# from userinput import keyboardInput
# mynumber = keyboardInput("Enter a number:", int, "Number must be Integer")
# print("Square of mynumber: ", mynumber * mynumber)

# You can set default values to the parameter
def calculateSI(principle, period=1, rate=6):
    interest = (principle * period * rate) / 100
    return interest

# HOW TO PASS SINGLE ARGUMENT
# How to make the arguments optional
print(calculateSI(1000)) 
# since we are not passing period, the default 1 is taken as value
# since we are not passing rate, the default 6 is taken as value

print(calculateSI(1000, 2))
# since we are passing 2 it overwrite the default 1
# since we are not passing rate, the default 6 is taken as value

# HOW TO PASS MULTIPLE ARGUMENT
print(calculateSI(1000, 2, 7))
# since we are passing 2 it overwrite the default 1
# since we are passing 7 it overwrite the default 6

# HOW TO PASS OPTIONAL ARGUMENT
# Even though it is optional they are still positional
# How to pass value for principle and rate only
# Keyword argument comes in
print(calculateSI(principle=1000, rate=7))

# There are some functions created without knowing how many arguments
# it is going to receive 
# traditionally for such problems we allow list as arguments
def total(mynumbers):
    result = 0
    for mynumber in mynumbers:
        result = result + mynumber
    return result

print(total([10, 20, 30, 40, 50, 60, 70]))
print(total([10, 20, 30, 40]))
print(total([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))

# However there are use cases where the caller is not able to pass 
# the values as a list
# this is also referred as "variable length arguments"
# In python you can handle this using some special syntax *
# The moment python sees * in the parameter it will convert all the
# arguments to a list automatically and pass the list to the function
def calculatetotal(*mynumbers):
    result = 0
    for mynumber in mynumbers:
        result = result + mynumber
    return result

print(calculatetotal(10, 20, 30, 40, 50, 60, 70))
print(calculatetotal(10, 20, 30, 40))
print(calculatetotal(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))

def plotGraph(graphType, colors, *data):
    print("Graph Type:", graphType)
    print("Colors:", colors)
    print("Data:", data)

plotGraph("boxplot", ["white", "black"], 10, 20, 30, 40, 50, 60)

def calculateTotalAverage(*data):
    total = 0
    for value in data:
        total = total + value
    average = total / len(data)
    # return [total, average]
    return total, average # python will automatically convert them to tuple

result = calculateTotalAverage(10, 20, 30, 40, 50, 60, 70, 80)
print(result[0], result[1])

totalvalue, average = calculateTotalAverage(10, 20, 30, 40, 50, 60, 70, 80)
print(totalvalue, average)

def printDetails(**arguments):
    print(arguments)

# when the function takes **parameter
# we can pass keyword argument as values
# the arguments are converted into a dictionary and pass to the function
printDetails(firstname="David", lastname="John")
