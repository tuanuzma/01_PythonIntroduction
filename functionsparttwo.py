# FUNCTIONAL PROGRAMMING
# 1. Passing function as an argument to another function
# 2. How to create inner function inside a function (nested functions)
# 3. Function can return an inner function

# Are we receiving David
# No we received the address location where the David Object is
def sayHello(user):
    print("Good Morning", user)

name = "David"
# are we passing David?
# No we are passing the address location where David Object is
sayHello(name)

def greeting():
    print("Welcome")

# What are we receiving at x
# The address location of the function body
def startSpeech(x):
    x()

startSpeech(greeting)
# we are passing function as an argument to another function
# remember greeting is just another variable holding the address
# location where the function body is (print("Welcome"))

# outer function
def authenticate(username, password):

    # inner function
    def simpleInterest(principle, period, rate):
        interest = (principle * period * rate) / 100
        return interest
    
    # you can call the inner function only from the outer function
    # you cannot call the inner function from outside the 
    # authenticate function
    if (username == 'admin' and password == 'pwd123'):
        interest = simpleInterest(1000, 1, 6)
        return interest
    else:
        return None
    
print(authenticate("admin", "pwd123"))

# There is no way for us to call the inner function
# Unless the outer function returns the inner function we can call
def authorize(username, password):

    def simpleInterest(principle, period, rate):
        interest = (principle * period * rate) / 100
        return interest
    
    if (username == 'admin' and password == 'pwd123'):
        # if admin password is correct we return simpleInterest
        return simpleInterest
    else:
        return None
    
result = authorize("admin", "pwd123") # inner function is assigned to result
print(result(1000, 2, 5)) # now we can call the inner function

# as long as the function returns an inner function 
# which can be called immediately using another ()
print(authorize("admin", "pwd123")(2000, 3, 4))



