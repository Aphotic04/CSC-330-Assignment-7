#I certify, that this computer program submitted by me is of my own work. Signed:
#Elisha Bjerkeset, Natasha Czaplewski, Ty Steinbach
#04/19/2025
#CSC 330
#Assignment 7
#Create a class for ASTNode

###################################
#####          ASTNode        #####
###################################
#Root node for ast
class ASTNode:
    def __init__(self):
        self.expressions = []

    def __repr__(self):
        return f"{self.expressions}"

###################################
#####          Check          #####
###################################
class Check:
    def __init__(self, accountNumber):
        self.accountNumber = accountNumber

    def __repr__(self):
        return f"Check Balance {self.accountNumber}"

###################################
#####          Create         #####
###################################
class Create:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def __repr__(self):
        return f"Create {self.firstName} {self.lastName}"

###################################
#####         Deposit         #####
###################################
class Deposit:
    def __init__(self, amount, accountNumber):
        self.amount = amount
        self.accountNumber = accountNumber

    def __repr__(self):
        return f"Deposit {self.amount} to {self.accountNumber}"

###################################
#####         Withdraw        #####
###################################
class Withdraw:
    def __init__(self, amount, accountNumber):
        self.amount = amount
        self.accountNumber = accountNumber

    def __repr__(self):
        return f"Withdraw {self.amount} from {self.accountNumber}"
