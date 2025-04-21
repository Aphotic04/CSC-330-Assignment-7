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
        #for x in range(tokens.length):
        print(tokens[0].TokenType)
        match tokens[0].TokenType:
            case TokenType.CREATE:
                print("1")
                return ASTNode.ASTNode(tokens[1], ASTNode.ASTNode(tokens[0]), ASTNode.ASTNode(tokens[2]))
            case TokenType.CHECK:
                print("2")
                return ASTNode.ASTNode(tokens[1], ASTNode.ASTNode(tokens[0]))
            case TokenType.DEPOSIT:
                print("3")
                return ASTNode.ASTNode(tokens[1], ASTNode.ASTNode(tokens[0]), ASTNode.ASTNode(tokens[2]))
            case TokenType.WITHDRAW:
                print("4")
                return ASTNode.ASTNode(tokens[1], ASTNode.ASTNode(tokens[0]), ASTNode.ASTNode(tokens[2]))
            
tokens1 = Lexer.Lexer.getTokens({"Deposit 14.14 to TS223344"})
tokens2 = Lexer.Lexer.getTokens({"Withdraw 50.14 from TS223344"})
tokens3 = Lexer.Lexer.getTokens({"Check Balance TS223344"})
tokens4 = Lexer.Lexer.getTokens({"Create John Doe"})

root1 = Parser.parse(tokens1)
print(root1)
print(root1.left)
print(root1.right)

root2 = Parser.parse(tokens2)
print(root2)
print(root2.left)
print(root2.right)

root3 = Parser.parse(tokens3)
print(root3)
print(root3.left)
print(root3.right)

root4 = Parser.parse(tokens4)
print(root4)
print(root4.left)
print(root4.right)