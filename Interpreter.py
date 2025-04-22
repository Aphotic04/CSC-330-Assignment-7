#I certify, that this computer program submitted by me is of my own work. Signed:
#Ty Steinbach, Natasha Czaplewski, Elisha Bjerkeset
#04/22/2025
#CSC 330
#Assignment 7
#Interpreter Class
import ASTNode
import Lexer
import Parser
import BankAccount

class Interpreter:
    def __init__(self):
        self.bank = {}
    def interpret(self, ast):
        expressions = ast.expressions
        for x in range(len(expressions)):
            currExpr = expressions[x]
            if (isinstance(currExpr, ASTNode.Create)):
                account = BankAccount.BankAccount(currExpr.firstName, currExpr.lastName)
                returnNum = account.getAccountNumber()
                self.bank[returnNum] = account
            if (isinstance(currExpr, ASTNode.Check)):
                try:
                    num = currExpr.accountNumber
                    self.bank[num].checkBalance(num)
                except:
                    print("Check Failed: Couldn't Find Account")
            if (isinstance(currExpr, ASTNode.Deposit)):
                try:
                    num = currExpr.accountNumber
                    self.bank[num].deposit(num, currExpr.amount)
                except:
                    print("Deposit Failed: Couldn't Find Account")
            if (isinstance(currExpr, ASTNode.Withdraw)):
                try:
                    num = currExpr.accountNumber
                    self.bank[num].withdraw(num, currExpr.amount)
                except:
                    print("Withdraw Failed: Couldn't Find Account")

'''tokens = Lexer.Lexer.getTokens(["Create John Doe"])

root = Parser.Parser.parse(tokens)
interpreter = Interpreter()
interpreter.interpret(root)
account = list(interpreter.bank.keys())[0]

tokens = Lexer.Lexer.getTokens([f"Deposit 14.14 to {account}", f"Withdraw 3.14 from {account}", f"Check Balance {account}"])
root = Parser.Parser.parse(tokens)
interpreter.interpret(root)'''

