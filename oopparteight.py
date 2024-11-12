# Every single Class in python is inherited from a
# base class called "object"
# There is a class called "object" in python
# And every class you create is inherited from the object Class
# all those __ methods are already created inside the class object
class Student():

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def sayFullName(self):
        return self.firstname + " " + self.lastname

class Graduate(Student):

    def __init__(self, firstname, lastname, graduatedyear):
        self.firstname = firstname
        self.lastname = lastname
        self.graduatedyear = graduatedyear

    # When parent class has a method and if you re-create
    # the same method in the child class it is called
    # Method Overriding
    def sayFullName(self):
        return super().sayFullName() + " " + str(self.graduatedyear)
    
    # __str__ is a method inside the class called object
    # and we have overridded the method in the Graduate class
    # __str__ method is called by print function
    def __str__(self):
        content = "First Name: " + self.firstname + "\n"
        content += "Last Name: " + self.lastname + "\n"
        content += "Graduated Year: " + str(self.graduatedyear)
        return content

khairi = Student("Khairi", "Abu Bakar")
peter = Graduate("Peter", "Parker", 2023)
print(peter.sayFullName())
print(peter) # peter.__str__() Print function automatically call

print(map(int, ["10", "20", "30"]))

