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
                amount = float(re.search("[0-9]+[.][0-9]+", line).group())
                account = re.search("([a-zA-Z]{2}[0-9]{6})$",line).group()
                
                amountToken = Token.Token(Token.TokenType.Number, amount)
                #amountToken.setType(Token.TokenType.Number)
                #amountToken.setValue(amount)

                accountToken = Token.Token(Token.TokenType.ACCOUNTID, account)
                #accountToken.setType(Token.TokenType.AccountNumber)
                #accountToken.setValue(amount)
                
                if (re.search("^Withdraw", line) and re.search("from", line)) or (re.search("^Deposit", line) and re.search("to", line)):
                    action = re.search("Withdraw|Deposit", line).group()

                    #actionToken = Token.Token

                    if (action == "Withdraw"):
                        actionToken = Token.Token(Token.TokenType.WITHDRAW, Token.TokenType.WITHDRAW)
                        #actionToken.setType(Token.TokenType.Withdraw)
                        #actionToken.setValue(Token.TokenType.Withdraw)
                    else:
                        actionToken = Token.Token(Token.TokenType.DEPOSIT, Token.TokenType.DEPOSIT)
                        #actionToken.setType(Token.TokenType.Deposit)
                        #actionToken.setValue(Token.TokenType.Deposit)
                    tokens.append(actionToken)
                    tokens.append(amountToken)
                    tokens.append(accountToken)
                    print(tokens)
                    
                    print("Withdrawal or deposit")
                else:
                    print("Verb and preposition don't match")
            else:
                print("What the heck happened?!")
        return tokens
Lexer.getTokens({"Deposit 14.14 to TS223344"})
Lexer.getTokens({"Withdraw 50.14 from TS223344"})
