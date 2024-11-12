# DECORATOR / ANNOTATOR
## Decorators are used to add more functionality into the existing function.
# Decorators are a very powerful and useful tool in Python 
# since it allows programmers to modify the behaviour of a function or class.
# without disturbing the original code that we have injected 
# some extra code to the function

# IMPORT DATETIME MODULE, CREATE OUTER AND INNER FUNCTION TO SEE HOW THE DECORATOR WORKS
# In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.
import datetime

def captureStartEndTime(func):

    def addCodeToCaptureStartEndTime(*arguments): # This take function as an argument
        now = datetime.datetime.now()
        print("Start Time:", now.time())
        result = func(*arguments)
        now = datetime.datetime.now()
        print("End Time", now.time())
        return result
    
    return addCodeToCaptureStartEndTime

@captureStartEndTime
def sayHello():
    print("Hello")

@captureStartEndTime
def simpleInterest(principle, period, rate):
    print("Inside Simple Interest...")
    return (principle * period * rate) / 100

# sayHello()
# captureStartEndTime(sayHello)()
sayHello() # I'm not calling the capture start time end time, I'm just calling to say hello like normal.
print(simpleInterest(1000, 1, 6)) # The simpleInterest is printing outside because after everything has been done
