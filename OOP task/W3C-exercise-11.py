from venv import create


class bank:
    def __init__(self):
        self.customers = {}

    def create_account(self, account_number, initial_balance = 0):
        if account_number not in self.customers:
            self.customers[account_number] = initial_balance
        else:
            print("account already exists")

    def deposit(self, account_number, deposit_amount):
        if account_number in self.customers:
            self.customers[account_number] += deposit_amount
        else:
            print("account does not exist")

    def withdraw(self, account_number, withdraw_amount):
        if account_number in self.customers:
            self.customers[account_number] -= withdraw_amount
        else:
            print("account does not exist")

    def show_balance(self,account_number):
        if account_number in self.customers:
            print(self.customers[account_number])
        else:
            print("account does not exist")

#main

my_bank = bank()

my_bank.create_account(1, 100)
my_bank.show_balance(1)
my_bank.deposit(1, 100)
my_bank.show_balance(1)
my_bank.withdraw(1, 20)
my_bank.show_balance(1)
