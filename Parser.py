#I certify, that this computer program submitted by me is of my own work. Signed:
#Ty Steinbach, Natasha Czaplewski, Elisha Bjerkeset
#04/21/2025
#CSC 330
#Assignment 7
#Parser Class

import ASTNode
import Lexer
from Token import TokenType

class Parser:
    #def __init__(self, tokens):
    #    self.tokens = tokens

    def parse(tokens):
        root = ASTNode.ASTNode()
        for x in range(len(tokens)):
            #print(tokens[x].TokenType)
            match tokens[x].TokenType:
                case TokenType.CREATE:
                    root.expressions.append(ASTNode.Create(tokens[x + 1].value, tokens[x + 2].value))
                    #ASTNode.ASTNode(self.tokens[1], ASTNode.ASTNode(self.tokens[0]), ASTNode.ASTNode(self.tokens[2]))
                case TokenType.CHECK:
                    root.expressions.append(ASTNode.Check(tokens[x + 1].value))
                    #return ASTNode.ASTNode(self.tokens[1], ASTNode.ASTNode(self.tokens[0]))
                case TokenType.DEPOSIT:
                    root.expressions.append(ASTNode.Deposit(tokens[x + 1].value, tokens[x + 2].value))
                    #return ASTNode.ASTNode(self.tokens[1], ASTNode.ASTNode(self.tokens[0]), ASTNode.ASTNode(self.tokens[2]))
                case TokenType.WITHDRAW:
                    root.expressions.append(ASTNode.Withdraw(tokens[x + 1].value, tokens[x + 2].value))
                    #return ASTNode.ASTNode(self.tokens[1], ASTNode.ASTNode(self.tokens[0]), ASTNode.ASTNode(self.tokens[2]))
                
        return root
            
tokens = Lexer.Lexer.getTokens({"Deposit 14.14 to TS223344", "Withdraw 50.14 from TS223344", "Check Balance TS223344", "Create John Doe"})


#root = Parser.parse(tokens)
#print(root)
