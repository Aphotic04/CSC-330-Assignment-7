#I certify, that this computer program submitted by me is of my own work. Signed:
#Ty Steinbach, Natasha Czaplewski, Elisha Bjerkeset
#04/22/2025
#CSC 330
#Assignment 7

import BankAccount
import Lexer
import Parser
from Interpreter import Interpreter

def initialize(bank):
    # Open the file in read mode
    file = open("accounts.txt", "r")
    for line in file:
        if line.strip():
            acc_id, balance = line.strip().split()
            acc = BankAccount.BankAccount("First", "Last")
            acc.setAccountNumber(acc_id)
            acc.setBalance(float(balance))
            bank[acc_id] = acc
    file.close()

def main():
    interpreter = Interpreter()
    initialize(interpreter.bank)
    
    #Print available accounts for testing purposes
    while True: 
        print("Available accounts:")
        for acc in interpreter.bank:
            print(f" - {acc}")
        

        accountID = input("Which account would you like to view/adjust? ").strip()
        #Error handling if account does not exist
        if accountID not in interpreter.bank:
            print("Account not found.")
            continue
           
        while True:
            print("\nSelect from the following options.")
            print("1. Make a deposit.")
            print("2. Make a withdrawal.")
            print("3. Check the balance.")
            print("4. Check another account.")
            print("5. Create a new account.")
            print("6. Run specification tests.")
            print("Exit")
            user_input = input("Selection: ").strip()
            
            #Deposit
            if user_input == "1":
                amount = float(input("Enter deposit amount: $"))
                interpreter.bank[accountID].deposit(accountID, amount)
                
            #Withdrawal
            elif user_input == "2":
                amount = float(input("Enter withdrawal amount: $"))
                interpreter.bank[accountID].withdraw(accountID, amount)
                
            #Check Balance
            elif user_input == "3":
                interpreter.bank[accountID].checkBalance(accountID)
                
            #Check another account
            elif user_input == "4":
                break
                
            #Create account
            elif user_input == "5":
                first = input("Enter first name: ")
                last = input("Enter last name: ")
                tokens = Lexer.Lexer.getTokens([f"Create {first} {last}"])
                root = Parser.Parser.parse(tokens)
                interpreter.interpret(root)
                print("Account created.")

            #Run spec tests
            elif user_input == "6":
                print("Running specification tests:")
            
            elif user_input.lower() == "exit":
                print("Thank you for banking with us!")
                return

if __name__ == "__main__":
    main()
