#I certify, that this computer program submitted by me is of my own work. Signed:
#Ty Steinbach, Natasha Czaplewski, Elisha Bjerkeset
#04/16/2025
#CSC 330
#Assignment 7
#Token Class

from enum import Enum

###################################
#####          Token          #####
###################################
class Token:
    #Constructor
    def __init__(self, TokenType, value = None):
        self.TokenType = TokenType
        self.value = value

    #Representation
    def __repr__(self):
        if self.value: return f"{self.TokenType}:{self.value}"
        return f"{self.TokenType}"

###################################
#####       TokenType         #####
###################################
class TokenType(Enum):
    NUMBER = "FLOAT"
    CREATE = "CREATE"
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"
    CHECK = "CHECK"
    ACCOUNTID = "ACCOUNTID"
    FIRSTNAME = "FIRSTNAME"
    LASTNAME = "LASTNAME"
