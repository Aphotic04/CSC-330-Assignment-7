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

###################################
#####       Interpreter       #####
###################################
class Interpreter:
    #Sets up bank dictionary
    def __init__(self):
        self.bank = {}
    #Interpret an ast
    def interpret(self, ast):
        expressions = ast.expressions
        #For each expression
        for x in range(len(expressions)):
            currExpr = expressions[x]
            #If Create, create a new account
            if (isinstance(currExpr, ASTNode.Create)):
                account = BankAccount.BankAccount(currExpr.firstName, currExpr.lastName)
                returnNum = account.getAccountNumber()
                self.bank[returnNum] = account
            #If Check, check account
            if (isinstance(currExpr, ASTNode.Check)):
                try:
                    num = currExpr.accountNumber
                    self.bank[num].checkBalance(num)
                except:
                    print("Check Failed: Couldn't Find Account")
            #If Deposit, deposit into account
            if (isinstance(currExpr, ASTNode.Deposit)):
                try:
                    num = currExpr.accountNumber
                    self.bank[num].deposit(num, currExpr.amount)
                except:
                    print("Deposit Failed: Couldn't Find Account")
            #If Withdraw, withdraw from account
            if (isinstance(currExpr, ASTNode.Withdraw)):
                try:
                    num = currExpr.accountNumber
                    self.bank[num].withdraw(num, currExpr.amount)
                except:
                    print("Withdraw Failed: Couldn't Find Account")
