#I certify, that this computer program submitted by me is of my own work. Signed:
#Elisha Bjerkeset, Natasha Czaplewski, Ty Steinbach
#04/19/2025
#CSC 330
#Assignment 7
#Create a class for ASTNode

class ASTNode:
    def __init__(self, Token, left = None, right = None):
        self.Token = Token
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.Token}"

class Check:
    def __init__(self, accountNumber):
        self.accountNumber = accountNumber

    def __repr__(self):
        return f"Check Balance {self.accountNumber}"

class Create:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def __repr__(self):
        return f"Create {self.firstName} {self.lastName}"

class Deposit:
    def __init__(self, amount, accountNumber):
        self.amount = amount
        self.accountNumber = accountNumber

    def __repr__(self):
        return f"Deposit {self.amount} to {self.accountNumber}"

class Withdraw:
    def __init__(self, amount, accountNumber):
        self.amount = amount
        self.accountNumber = accountNumber

    def __repr__(self):
        return f"Withdraw {self.amount} from {self.accountNumber}"

'''newCheckNode = ASTNode(Check("TS112233"))
newCreateNode = ASTNode(Create("Ty", "Steinbach"))
newDepositNode = ASTNode(Deposit(1122, "TS112233"))
newWithdrawNode = ASTNode(Withdraw(1122, "TS112233"))
print(newCheckNode)
print(newCreateNode)
print(newDepositNode)
print(newWithdrawNode)'''
