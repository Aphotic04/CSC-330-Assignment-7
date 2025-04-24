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

    #Loop for main logic
    stay = True
    while stay:
        #Print options
        print("\nSelect from the following options.")
        print("1. Login to an account.")
        print("2. Create new account")
        print("3. Use Console (Actually using our language)")
        print("4. Unit Test")
        print("5. Exit.")

        userInput = input("Selection: ").strip()

        #Switch statement for user input
        match userInput:
            case "1": #Log into accout
                #Print available accounts
                print("Available accounts:")
                for acc in interpreter.bank:
                    print(f" - {acc}")
                    
                accountID = input("Enter an account to login to  ").strip()
                
                #Error handling if account does not exist
                if accountID not in interpreter.bank:
                    print("Account not found.")
                else: #If account exists
                    #Input loop for logged in logic
                    stayLogged = True
                    while stayLogged:
                        #Print options
                        print("\nSelect from the following options.")
                        print("1. Make a deposit.")
                        print("2. Make a withdrawal.")
                        print("3. Check the balance.")
                        print("4. Log out.")
                        
                        userInput = input("Selection: ").strip()

                        #Switch for user input
                        match userInput:
                            case "1": #Make deposit based on input
                                #Get input
                                userInput = input("Enter the amount to deposit. Example: '10', '15.55': ")

                                #Ensures input is digit and compiles input
                                if isfloat(userInput):
                                    inputString = f"Deposit {userInput} to {accountID}"
                                    inputArray = [inputString]
                                    previous_balance = interpreter.bank[accountID].getBalance()
                                    runCommands(inputArray, interpreter)
                                    current_balance = interpreter.bank[accountID].getBalance()
                                    testing(test = "test_deposit", previous = previous_balance, current = current_balance, amount = float(userInput))
                                else:
                                    print("Invalid Entry")
                            case "2": #Make withdrawl based on input
                                #Get input
                                userInput = input("Enter the amount to withdraw. Example: '10', '15.55': ")

                                #Ensures input is digit and compiles input
                                if isfloat(userInput):
                                    inputString = f"Withdraw {userInput} from {accountID}"
                                    inputArray = [inputString]
                                    previous_balance = interpreter.bank[accountID].getBalance()
                                    runCommands(inputArray, interpreter)
                                    current_balance = interpreter.bank[accountID].getBalance()
                                    testing(test = "test_withdraw", previous = previous_balance, current = current_balance, amount = float(userInput))
                                else:
                                    print("Invalid Entry")
                            case "3": #Check balance of account
                                #Compiles command
                                inputString = f"Check Balance {accountID}"
                                inputArray = [inputString]
                                runCommands(inputArray, interpreter)
                            case "4": #Log out
                                stayLogged = False
                            case default: #Incorrect input handling
                                print("Invalid Option")
            case "2": #Create new account
                #Get input
                userInput = input("Enter the first and last name only. Example: 'Ty Steinbach': ")

                #Compile commands
                try:
                    inputString = f"Create {userInput}"
                    inputArray = [inputString]
                    runCommands(inputArray, interpreter)
                except:
                    print("Invalid Entry")
            case "3": #Use console
                #Print instructions
                print("To leave, type 'Exit'\n")
                print("Command syntax:\nCreate firstName lastName\nCheck Balance accountNumber\nWithraw decimalNumber from accountNumber\nDeposit decimalNumber to accountNumber")
                print("\n\n")

                #Input loop for console logic
                stayConsole = True
                while stayConsole:
                    commands = []
                    userInput = input("Command: ")
                        
                    if userInput == "Exit": #Exit
                        stayConsole = False
                    else: #Compile
                        commands.append(userInput)
                        try:
                            runCommands(commands, interpreter)
                        except:
                            print("Incorrect Syntax")
            case "4": #Run unit tests
                specification_tests()
            case "5": #Exit
                stay = False
            case default: #For any other input
                print("Invalid Option")
        
                        
            
                    

###################################
#####       runCommands       #####
###################################
#Runs tests
def runCommands(commands, interpreter):
    tokens = Lexer.Lexer.getTokens(commands)
    AST = Parser.Parser.parse(tokens)
    interpreter.interpret(AST)

###################################
#####    specification_tests  #####
###################################
#Runs tests
def specification_tests():
    testing(test = "test_create", account = BankAccount.BankAccount("John", "Doe"))
    testing(test = "test_deposit", previous = 100.00, current = 150.00, amount = 50.00)
    testing(test = "test_withdraw", previous = 100.00, current = 50.00, amount = 50.00 )

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
            print("Expected value after deposit: " + str(self.previous + self.amount))
            print("Actual value after deposit: " + str(self.current))
            self.assertEqual(self.current, self.previous + self.amount)

        def test_withdraw(self):
            #Testing the balance
            print("Expected value after deposit: " + str(self.previous - self.amount))
            print("Actual value after deposit: " + str(self.current))
            self.assertEqual(self.current, self.previous - self.amount)

    #Loading the tests in the class and a runner for those tests
    suite = unittest.TestSuite()

    #Adding the specified test to run
    if test:
        suite.addTest(Test(test))

    #Running Test
    unittest.TextTestRunner().run(suite)   

###################################
#####      Float Checking     #####
###################################
#Float checker
def isfloat(s):
    try:
        float(s)
        return True
    except:
        return False
    
#Calling main
if __name__ == "__main__":
    main()
