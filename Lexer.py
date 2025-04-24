#I certify, that this computer program submitted by me is of my own work. Signed:
#Elisha Bjerkeset, Natasha Czaplewski, Ty Steinbach
#04/18/2025
#CSC 330
#Assignment 7
#Create a lexer for a DSL

import re
import Token

###################################
#####          Lexer          #####
###################################
class Lexer:
    def getTokens(linesCode):
        tokens = []
        for line in linesCode:
            #If string matches a deposit or withdraw
            if re.search("^((Withdraw|Deposit) [0-9]+[.][0-9]+ (to|from) [a-zA-Z]{2}[0-9]{6})$", line):
                #Get amount/account info
                amount = float(re.search("[0-9]+[.][0-9]+", line).group())
                account = re.search("([a-zA-Z]{2}[0-9]{6})$", line).group()
                #Create tokens from amount/account
                amountToken = Token.Token(Token.TokenType.NUMBER, amount)
                accountToken = Token.Token(Token.TokenType.ACCOUNTID, account)

                #Ensuring verb and preposition match
                if (re.search("^Withdraw", line) and re.search("from", line)) or (re.search("^Deposit", line) and re.search("to", line)):
                    #Create appropriate tokens
                    action = re.search("Withdraw|Deposit", line).group()

                    if (action == "Withdraw"):
                        actionToken = Token.Token(Token.TokenType.WITHDRAW, Token.TokenType.WITHDRAW)

                    else:
                        actionToken = Token.Token(Token.TokenType.DEPOSIT, Token.TokenType.DEPOSIT)

                    #And append
                    tokens.append(actionToken)
                    tokens.append(amountToken)
                    tokens.append(accountToken)
                    
                else:
                    print("Verb and preposition don't match")
            
            #Mathces Check Balance
            elif re.search("^Check Balance [a-zA-Z]{2}[0-9]{6}$", line):
                #Gets information and creates tokens
                account = re.search("([a-zA-Z]{2}[0-9]{6})$", line).group()

                actionToken = Token.Token(Token.TokenType.CHECK, Token.TokenType.CHECK)
                accountToken = Token.Token(Token.TokenType.ACCOUNTID, account)

                #Append tokens
                tokens.append(actionToken)
                tokens.append(accountToken)
            #Mathces Create name
            elif re.search("Create [a-zA-Z]+ [a-zA-Z]+$", line):
                #Extract names to assist in accountID creation
                names = re.findall("[a-zA-Z]+", line)
                firstName, lastName = names[1], names[2]
                
                #Create appropriate tokens
                actionToken = Token.Token(Token.TokenType.CREATE, Token.TokenType.CREATE)
                firstNameToken = Token.Token(Token.TokenType.FIRSTNAME, firstName)
                lastNameToken = Token.Token(Token.TokenType.LASTNAME, lastName)

                #Append tokens
                tokens.append(actionToken)
                tokens.append(firstNameToken)
                tokens.append(lastNameToken)
            else:
                print("Lexer Error: Incorrect Syntax")
        return tokens
