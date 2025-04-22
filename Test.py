#I certify, that this computer program submitted by me is of my own work. Signed:
#Ty Steinbach, Natasha Czaplewski, Elisha Bjerkeset
#04/22/2025
#CSC 330
#Assignment 7
#specification_tests() function

import unittest
import BankAccount

def specification_tests(test, account = None, previous = None, current = None, amount = None):
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

specification_tests(test = "test_create", account = BankAccount.BankAccount("John", "Doe"))
specification_tests(test = "test_deposit", previous = 100, current = 150, amount = 50)
specification_tests(test = "test_withdraw", previous = 100, current = 50, amount = 50)