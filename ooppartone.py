# Class are nothing but blue print

# Methods are nothing but functions inside the class
# Methods are different from functions in number of parameters
# Methods must have atleast 1 parameter
# When we call the methods we no need to pass argument for the first parameter
# The first parameter is conventionally called self

# Properties are nothing but variables inside the class
# Properties are always prefixed with first parameter of the method

# CREATE CLASS
# We can create a class using keyword class
class Patient:
    # unlike other tradional programming languages we cannot declare the variables
    # without the value in python, however the properties must be declared
    # and initialized
    # we have a special method called constructor (__init__)
    # the constuctor will get executed whenever a new object is created

    # CREATE NEW OBJECT BY USING METHOD CONSTRUCTOR AND PUT PARAMETER TO INITIALIZE THE VARIABLE
    def __init__(self):
        # Constructor is the place where we are going to create all the properties
        # and initialize the properties
        print("Object created successfully")
        self.firstname = ""
        self.lastname = ""
        self.icnumber = ""
        self.medicineprices = []
        self.appointmentdate = ""
        self.appointmenttime = ""

    # ANOTHER METHOD TO PRINT VALUE
    # let us create one more method to print the firstname, lastname and icnumber
    def info(self):
        print("First Name:", self.firstname)
        print("Last Name:", self.lastname)
        print("IC Number:", self.icnumber)
        print("Appointment Date:", self.appointmentdate)
        print("Appointment Time:", self.appointmenttime)

    # METHOD IS RETURNING VALUE
    def doPayment(self):
        total = 25
        for price in self.medicineprices:
            total = total + price
        return total
    
    # METHOD IS TAKING MORE THAN 1 PARAMETER
    def doAppointment(self, strdate, strtime):
        self.appointmentdate = strdate
        self.appointmenttime = strtime

# CREATE FIRST OBJECT
# Let us create our first Object
peter = Patient() # object creation is similar to function call
# class name followed by () which will return Object instance of the Class
# When we call the class the constructor gets executed automatically
print(type(peter))

# CREATE ONE MORE OBJECT
# Let us create one more object
khairi = Patient()

# CREATE OBJECT WITH VALUES
# Let us set the object with values
peter.firstname = "Peter"
peter.lastname = "Parker"
peter.icnumber = 720102121234
peter.medicineprices = [6.20, 12.80, 7.10]
# the state is in memory so it can print the values anytime
peter.doAppointment("13-08-2024", "6:15PM")
peter.info()
print("Amount to be paid:", peter.doPayment())
khairi.info()

# class list:
    # def append(self, x):
        # pass
    # def extend(self, y):
        # pass

# fruits = list(["apple", "orange", "mango"])
# python give us the flexibility, through which we can create list without use the class list
# fruits = ["apple", "orange", "mango"]
    
