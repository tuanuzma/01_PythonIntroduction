# Constructor is a special method that gets executed automatically
# Constructor takes atleast 1 parameter (called self)
# The value for the first parameter (argument) no need to pass
# Object creation. 
# To create some objects there are some compulsory values
# must be passed
# For example no point of creating Patient Object without
# firstname, lastname and ic number

class Patient:

    # We are modifing the constructor to take 3 compulsory parameters
    # We will assign the parameter values to the property directly
    def __init__(self, firstname, lastname, icnumber):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = icnumber
        self.medicineprices = []
        self.appointmentdate = ""
        self.appointmenttime = ""

    def info(self):
        print("First Name:", self.firstname)
        print("Last Name:", self.lastname)
        print("IC Number:", self.icnumber)
        print("Appointment Date:", self.appointmentdate)
        print("Appointment Time:", self.appointmenttime)

    def doPayment(self):
        total = 25
        for price in self.medicineprices:
            total = total + price
        return total
    
    def doAppointment(self, strdate, strtime):
        self.appointmentdate = strdate
        self.appointmenttime = strtime

peter = Patient("Peter", "Parker", 720102121234) 
# we should not let peter (Patient) object to be
# created without firstname, lastname and icnumber
peter.info()

khairi = Patient("Khairi", "Abu Bakar", 760102121234)
khairi.info()

# Important Notes:
# When you call peter.info()
# Python pass "peter" (object) to the info method automatically
# When you call khairi.info()
# Python pass "khairi" (object) to the info method automatically

# I can access the property outside the class
# It is publicly visible
# Somemore we cannot control the assignment of illegal values
khairi.firstname = "Something"
# Unless we retrict the property access by introducing a middle layer
# This is called Encapsulation
