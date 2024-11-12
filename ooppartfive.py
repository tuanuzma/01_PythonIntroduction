# Bank will give me ATM Card
# Bank started giving Credit Card
# Bank started giving Debit Card
# Bank gives you Bank Card extends the features of
# Atm Card, Credit Card and Debit Card

class AtmCard:

    def __init__(self):
        print("ATM Card")

class CreditCard:

    def __init__(self):
        print("Credit Card")

    def info(self):
        print("Info: Credit Card")

class DebitCard:

    def __init__(self):
        print("Debit Card")

    def info(self):
        print("Info: Debit Card")

class BankCard(AtmCard, CreditCard, DebitCard):

    def __init__(self):
        super().__init__() # which super are you referring to
        # Method Resolution Order (MRO) it says
        # go from left to right until it matches the method
        # If one of the parent happens to have that method
        # it gets executed and thats it
        pass

mybankcard = BankCard()
mybankcard.info() # the BankCard do not have info method
# However BankCard is inherited from AtmCard, CreditCard and DebitCard
# If any one of the above mention class has the info method it will get executed
# Based on MRO (Method Resolution Order) AtmCard is the first parent
# however it does not have info method. CreditCard is the second parent
# it has the info method and that gets executed.

