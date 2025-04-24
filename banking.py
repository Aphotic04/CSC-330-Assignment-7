#I certify, that this computer program submitted by me is of my own work. Signed:
#Ty Steinbach, Natasha Czaplewski, Elisha Bjerkeset
#04/24/2025
#CSC 330
#Assignment 7

import BankAccount
import Lexer
import Parser
import Interpreter
import unittest

###################################
#####       initialize        #####
###################################
#Loads new accounts into bank
def initialize(interpreter):
    #Open the file in read mode
    file = open("accounts.txt", "r")
    commands = []
    
    #Places lines in array
    for line in file:
        if line.strip():
            commands.append(line.strip())

    #Compiles data
    tokens = Lexer.Lexer.getTokens(commands)
    AST = Parser.Parser.parse(tokens)
    interpreter.interpret(AST)
    file.close()

###################################
#####           main          #####
###################################
def main():
    #New interpreter and call initialize
    interpreter = Interpreter.Interpreter()
    initialize(interpreter)
    
    #Print available accounts
    print("Available accounts:")
    for acc in interpreter.bank:
        print(f" - {acc}")

    #Print Instructions
    print("To leave, type 'Exit'\n")
    print("To run specification testing, type 'Test'\n")
    print("Command syntax:\nCreate firstName lastName\nCheck Balance accountNumber\nWithraw decimalNumber from accountNumber\nDeposit decimalNumber to accountNumber")
    print("\n\n")

    #Input loop
    stay = True
    while stay:
        commands = []
        userInput = input("Command: ")
        
        if userInput == "Exit": #Exit
            stay = False
        elif userInput == "Test": #Run Tests
            specification_tests()
        else: #Compile
            commands.append(userInput)
            try:
                tokens = Lexer.Lexer.getTokens(commands)
                AST = Parser.Parser.parse(tokens)
                interpreter.interpret(AST)
            except:
                print("Incorrect Syntax")

###################################
#####    specification_tests  #####
###################################
#Runs tests
def specification_tests():
    testing(test = "test_create", account = BankAccount.BankAccount("John", "Doe"))
    testing(test = "test_deposit", previous = 100, current = 150, amount = 50)
    testing(test = "test_withdraw", previous = 100, current = 50, amount = 50)

###################################
#####         testing         #####
###################################
#Unit testing
def testing(test, account = None, previous = None, current = None, amount = None):
    class Test(unittest.TestCase):
        #Getting variables
        def setUp(self):
            self.account = account
            self.previous = previous
            self.current = current
            self.amount = amount

        def test_create(self):
            #Asserting if the account number matched the expected regex
            first = self.account.getFirstName()[0]
            last = self.account.getLastName()[0]
            pattern = rf"^{first}{last}\d{{6}}$"
            self.assertRegex(self.account.getAccountNumber(), pattern)

        def test_deposit(self):
            #Testing the balance
            self.assertEqual(self.current, self.previous + self.amount)

        def test_withdraw(self):
            #Testing the balance
            self.assertEqual(self.current, self.previous - self.amount)

    #Loading the tests in the class and a runner for those tests
    suite = unittest.TestSuite()

    #Adding the specified test to run
    if test:
        suite.addTest(Test(test))

    #Running Test
    unittest.TextTestRunner().run(suite)   

#Calling main
if __name__ == "__main__":
    main()
