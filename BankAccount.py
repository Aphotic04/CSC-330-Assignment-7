#I certify, that this computer program submitted by me is of my own work. Signed:
#Ty Steinbach, Natasha Czaplewski, Elisha Bjerkeset
#04/16/2025
#CSC 330
#Assignment 7
#BankAccount Class
import random

###################################
#####      BankAccount        #####
###################################
class BankAccount:

    #Constructor
    def __init__(self, firstName, lastName):
        self.__firstName = firstName.upper()
        self.__lastName = lastName.upper()
        self.__accountNumber = firstName[0].upper() + lastName[0].upper()
        for x in range(6):
            self.__accountNumber += str(random.randint(0, 9))
        self.__balance = 0

    #Print as
    def __repr__(self):
        return f"{self.__firstName} {self.__lastName}\n{self.__accountNumber}\nBalance: {self.__balance}"

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
    def withdraw(self, accountNum, amount):
        if (accountNum == self.__accountNumber):
            if amount > self.__balance:
                print("Insufficient funds!")
            else:
                self.setBalance(self.getBalance() - amount)
                print(f"New Balance: {self.__balance}")
        
    #Depositing money
    def deposit(self, accountNum, amount):
        if (accountNum == self.__accountNumber):
            self.setBalance(self.getBalance() + amount)
            print(f"New Balance: {self.__balance}")
            
    #Checking balance
    def checkBalance(self, accountNum):
        if (accountNum == self.__accountNumber):
            print("Balance for this account is: $" + str(self.getBalance()))
