#Ty Steinbach, Natasha Czaplewski, Elisha Bjerkeset
#CSC 330
#Assignment 7
import random

class BankAccount:

    #Constructor
    def __init__(self, firstName, lastName):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__accountNumber = firstName[0] + lastName[0]
        for x in range(6):
            self.__accountNumber += str(random.randint(0, 9))
        self.__balance = 0

    #Getters and Setters
    def getFirstName(self):
        return self.__firstName
    def setFirstName(self, firstName):
        self.__firstName = firstName

    def getLastName(self):
        return self.__lastName
    def setLastName(self, lastName):
        self.__lastName = lastName

    def getAccountNumber(self):
        return self.__accountNumber
    def setAccountNumber(self, accountNumber):
        self.__accountNumber = accountNumber

    def getBalance(self):
        return self.__balance
    def setBalance(self, balance):
        self.__balance = balance

    #Withdraw (error handling for insufficient funds)    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.setBalance(self.getBalance() - amount)
        
    #Depositiing money
    def deposit(self, amount):
        self.setBalance(self.getBalance() + amount)
            
    #Withdrawing money
    def checkBalance(self):
        print("Balance for this account is: $" + str(self.getBalance()))

example = BankAccount("John", "Smith")
print(example.getAccountNumber())
example.checkBalance()
example.deposit(100)
example.checkBalance()
example.withdraw(50)
example.checkBalance()