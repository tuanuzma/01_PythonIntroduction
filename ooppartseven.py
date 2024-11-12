class AtmCard:
    def __init__(self):  # In python, _init__ is an instance method that initializes a newly created object
        print("ATM Card")

class CreditCard:
    def __init__(self):
        print("Credit Card")
    def info(self):   # The method takes the object as its first argument (self),
        print("Info: Credit Card")  # followed by any additional arguments that need to be passed to it

class DebitCard:
    def __init__(self, accountholder):
        print("Debit Card")
        self.accountholder = accountholder
    def info(self):
        print("Info: Debit Card", self.accountholder)

class BankCard(AtmCard, CreditCard, DebitCard):
    def __init__(self, accountholder):
        super().__init__()
        DebitCard.__init__(self, accountholder)

mybankcard = BankCard("Khairi") # mybankcard is an instance of BankCard Class
mybankcard.info() # calling instance method info
DebitCard.info(mybankcard) # even though it looks like
# we are calling a class method, we are not calling class method
# we are calling instance method. 
# Calling instance method via Class
