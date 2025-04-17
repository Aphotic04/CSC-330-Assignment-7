#I certify, that this computer program submitted by me is of my own work. Signed:
#Ty Steinbach, Natasha Czaplewski, Elisha Bjerkeset
#04/16/2025
#CSC 330
#Assignment 7
#Token Class

from enum import Enum

class Token:
    def __init__(self, Tokentype, value = None, pos_start = None, pos_end = None):
        self.Tokentype = Tokentype
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()
        if pos_end:
            self.pos_end = pos_end.copy()

    def __repr__(self):
        if self.value: return f"{self.Tokentype}:{self.value}"
        return f"{self.Tokentype}"

class TokenType(Enum):
    Number = "FLOAT"
    CREATE = "CREATE"
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"
    CHECK = "CHECK"
    #TT_FOR = "FROM"
    #TT_TO = "TO"
    ACCOUNTID = "ACCOUNTID"
    FIRSTNAME = "FIRSTNAME"
    LASTNAME = "LASTNAME"


class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char = None):
        self.idx += 1
        self.col += 1

        if current_char == "\n":
            self.ln += 1
            self.col = 0

        return self
    
    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)