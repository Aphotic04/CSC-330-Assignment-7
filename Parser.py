#I certify, that this computer program submitted by me is of my own work. Signed:
#Ty Steinbach, Natasha Czaplewski, Elisha Bjerkeset
#04/21/2025
#CSC 330
#Assignment 7
#Parser Class

import ASTNode
import Lexer
from Token import TokenType

###################################
#####         Parser          #####
###################################
class Parser:
    #Parses tokens
    def parse(tokens):
        #Create new root node
        root = ASTNode.ASTNode()
        for x in range(len(tokens)):
            #For the appropriate token type, create appropriate tokens and their respective dependant values
            match tokens[x].TokenType:
                case TokenType.CREATE:
                    root.expressions.append(ASTNode.Create(tokens[x + 1].value, tokens[x + 2].value))
                case TokenType.CHECK:
                    root.expressions.append(ASTNode.Check(tokens[x + 1].value))
                case TokenType.DEPOSIT:
                    root.expressions.append(ASTNode.Deposit(tokens[x + 1].value, tokens[x + 2].value))
                case TokenType.WITHDRAW:
                    root.expressions.append(ASTNode.Withdraw(tokens[x + 1].value, tokens[x + 2].value))
        return root
