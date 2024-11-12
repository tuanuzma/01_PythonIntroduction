# So definitely there is a switch on off and all those things happening because 
# at this point will be loaded in one memory location and then the address is 
# assigned to a variable called student and 
# then this memory location is a callable memory location.

# Class
class Student:

    # Class Variables are declared inside the class outside methods
    # Class Variables are not prefixed with self
    count = 0

    # Constructor
    def __init__(self):
        # Properties
        self.firstname = ""
        self.lastname = ""
        # the class variable is accessed without self
        # with classname
        Student.count = Student.count + 1

    # Method
    def info(self):
        # local variable
        message = "hello"
        print(self.firstname)
        print(self.lastname)

    # In a class there can be a method which does not take
    # self as argument
    # These methods are called "Class Methods"
    def howMany():
        return Student.count

# Object
peter = Student()
# Instance Variables
peter.firstname = "Peter"
peter.lastname = "Parker"
# Call the method via Instances
peter.info() # Instance Method
# To access the class variable you no need instance
# just use the class name
# Student.count += 1

khairi = Student()
# Instance Variables
khairi.firstname = "Peter"
khairi.lastname = "Parker"
# Call the method via Instances
khairi.info() # Instance Method
# To access the class variable you no need instance
# just use the class name
# Student.count += 1

print(Student.count)

# To access the class method you no need instances
# just use the class name
print("How many:", Student.howMany())

