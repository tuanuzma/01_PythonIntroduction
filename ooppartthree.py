# ENCAPSULATION

# Encapsulation is a fundamental object-oriented principle in Python.
# It protects your classes from accidental changes or deletions and 
# promotes code reusability and maintainability
# Illegalnames can make major risk to the validation of data.

# We can access the property outside the class
# Properties is publicly visible
# We cannot control the assignment of illegal values
# khairi.firstname = "Something"

# There are 2 steps in Encapsulation (getter and setter method)
# 1) Make the property private

class Patient:

    def __init__(self, firstname, lastname, icnumber):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__icnumber = icnumber
    
    # Let us create getter method and setter method
    def getFirstName(self):
        return self.__firstname
    
    # This setter method becomes a middle layer for us
    # to modify the private members
    def setFirstName(self, firstname):
        illegalnames = ["", "something", "none", "null", "-"]
        if (firstname not in illegalnames):
            self.__firstname = firstname

    # You can create a fake property by passing getter method
    # and the setter method to the built in function called property()
    # We can say this as a fake property for __firstname
    firstname = property(getFirstName, setFirstName)

    def info(self):
        print("First Name:", self.__firstname)
        print("Last Name:", self.__lastname)
        print("IC Number:", self.__icnumber)

peter = Patient("Petar", "Parker", 720102121234)
# Because you introduce __ before the property
# the property becomes "private"
# Which means the value cannot be assigned to the property
# peter.__firstname = "Peter"
peter.setFirstName("Peter")
print("First Name:", peter.getFirstName())
peter.firstname = "Peter"
print("Fist Name: ", peter.firstname)

peter.info()
