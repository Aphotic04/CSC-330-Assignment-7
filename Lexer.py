#I certify, that this computer program submitted by me is of my own work. Signed:
#Elisha Bjerkeset, Natasha Czaplewski, Ty Steinbach
#04/16/2025
#CSC 330
#Assignment 7
#Create a lexer for a DSL

import re
import Token

class Lexer:
    def getTokens(linesCode):
        tokens = []
        for line in linesCode:
            if re.search("^((Withdraw|Deposit) [0-9]+[.][0-9]+ (to|from) [a-zA-Z]{2}[0-9]{6})$", line):
                amount = float(re.search("[0-9]+[.][0-9]+", line))
                account = re.search("([a-zA-Z]{2}[0-9]{6})$",line)
                
                amountToken = Token.Token
                amountToken.setType(Token.TokenType.Number)
                amountToken.setValue(amount)

                accountToken = Token.Token
                accountToken.setType(Token.TokenType.AccountNumber)
                accountToken.setValue(amount)
                
                if (re.search("^Withdraw", line) and re.search("from", line)) or (re.search("^Deposit", line) and re.search("to", line)):
                    action = re.search("Withdraw|Deposit")

                    actionToken = Token.Token

                    if (action == "Withdraw"):
                        actionToken.setType(Token.TokenType.Withdraw)
                        actionToken.setValue(Token.TokenType.Withdraw)
                    else:
                        actionToken.setType(Token.TokenType.Deposit)
                        actionToken.setValue(Token.TokenType.Deposit)
                    tokens.append(actionToken)
                    tokens.append(amountToken)
                    tokens.append(accountToken)
                    
                    print("Withdrawal or deposit")
                else:
                    print("Verb and preposition don't match")
            else:
                print("What the heck happened?!")
        return tokens
Lexer.getTokens({"Deposit 14.14 to TS223344"})
