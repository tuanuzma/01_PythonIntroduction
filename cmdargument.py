# COMMAND LINE ARGUMENT (IMPORTANT)
# sys is a built in module
# It has many variables and functions inside
# one of the variable is argv
import sys

print(sys.argv)

# to find the sum of values (command line argument)
# python cmdargument.py 10 20 30 40 50
values = sys.argv
total = 0
for value in values[1:]:
    total = total + int(value)

print("Sum of numbers: ", total)

mylist = [10, 20, 30, 40, 50]
mytuple = (10, 20, 30, 40, 50)

print("sys.getsizeof a list:", sys.getsizeof(mylist))
print("sys.getsizeof a tuple:", sys.getsizeof(mytuple))

mynestedlist = [10, 20, 30, 40, 50, [60, 70, 80, 90]]
print("sys.getsizeof a nested list (wrong):", sys.getsizeof(mynestedlist))
mynestedtuple = (10, 20, 30, 40, 50, (60, 70, 80, 90))
print("sys.getsizeof a nested list (wrong):", sys.getsizeof(mynestedtuple))

# PIP INSTALL THIRDPARTY MODULE USING OBJSIZE
# objsize is not a built in module
# it is a thirdparty module which is hosted at pypi repository
# you must install it using pip install thirdpartymodule
# pip install objsize
import objsize

# MODULE .GET_DEEP_SIZE()
# get_deep_size is not a method
# eventhough we have the signature object.method
# in this particular case is is not object.method
# it is module.function
print("objsize.get_deep_size:", objsize.get_deep_size(mynestedlist))
print("objsize.get_deep_size:", objsize.get_deep_size(mynestedtuple))

# PIP INSTALL THIRDPARTY MODULE USING MEMORY_PROFILER
# memory_profiler is not a built in module
# it is a thirdparty module which is hosted at pypi repository
# you must install it using pip install thirdpartymodule
# pip install memory_profiler
from memory_profiler import profile

@profile # Decorator
def load_data():
    a = [i for i in range(0, 1000)]
    b = [i ** i for i in range(0, 1000)]
    return a, b

load_data()

# SYS MODULE
# provides various functions and variables that are used 
# to manipulate different parts of the Python runtime environment.
# There is another important variable in this sys module
# path is the variable
# this tells python path where to look for modules
# sys.path is list of object 
# so when we actually want to add some item into the list, we use the append method.
print(sys.path)
sys.path.append("C:\\mymodules") 
print(sys.path)

from mylibrary import sayHello
sayHello()
