# NameError
# the variable must be defined and initialzied
# before we use it (access it)

# print(name) # NameError: name 'name' is not defined
# step = step + 1 # NameError: name 'step' is not defined

# -----------------------------------------------------------
# TypeError

# len is a built in function that can tell us how many characters
# we have in a string
myname = "Uzma"
print(len(myname)) 
# the above function is exepecting you to send a string
# but what if you send a number
# print(len(42))

# the arithmatic equation is expecting you to have number 
# but you are having string
# x = "10"
# y = 5
# z = x - y

# -----------------------------------------------------------
# ValueError
# int function will convert string to integer
# the function is excepting you to send "string"

# print(int("10"))
# print(int("apple"))

# SyntaxError
# rules while doing programming
# when we call the function function name must be followed by ()

# print "Hello"
