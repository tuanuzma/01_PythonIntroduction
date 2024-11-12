# Let us talk about Relationship

class Address:

    def __init__(self, street_one, city, postcode, state, country):
        self.street_one = street_one
        self.city = city
        self.postcode = postcode
        self.state = state
        self.country = country

class Customer:

    def __init__(self, firstname, lastname, icnumber):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = icnumber
        # has-a relationship Customer has many addresses
        self.addresses = []


# VipCustomer is a Customer
# VipCustomer will inherit all the properties and methods of Customer
# In this relationship Customer is the parent and VipCustomer is the child
class VipCustomer(Customer):

    def __init__(self, firstname, lastname, icnumber, discount):
        # we are calling to initialize the variables which is declared 
        # in the __init__ method of customer class
        super().__init__(firstname, lastname, icnumber)
        self.discount = discount
        self.addresses = []

peter = Customer("Peter", "Parker", 720102121234)
addressone = Address("15 Lorong 5/92", "Petaling Jaya", 67384, "Selangor", "Malaysia")
peter.addresses.append(addressone)
addresstwo = Address("Jalan SS2/233", "Subang Jaya", 57484, "Selangor", "Malaysia")
peter.addresses.append(addresstwo)
aida = VipCustomer("Aidawaty", "Abdullah", 790102121234, 10)

print(type(peter))
print(type(aida))