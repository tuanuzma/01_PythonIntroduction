# MONKEY PATCHING
# If we want to add a new method to the existing class
# then we use monkey patching

class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

# First method is you can extend and create a new class
# and add the new methods inside the newly created class
class MyStudent(Student):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
    def sayFullName(self):
        return self.firstname + self.lastname
    
# Second method is using monkey patching
# I want to add sayFullName method to the Student class
def sayFullName(cls): # cls is just a variable
    cls.sayFullName = lambda self: self.firstname + " " + self.lastname
    return cls

def sayHello(self):
    print("Hello", self.firstname, self.lastname)

Student = sayFullName(Student)
peter = Student("Peter", "Parker")
# Monkey Patching
print(peter.sayFullName())
Student.greeting = sayHello # taking the address location of a function 
# and assign it to a property in the class
khairi = Student("Khairi", "Abu Bakar")
khairi.greeting() # since we have () python will go to that address location
# see got any code there if got then it will execute the code
