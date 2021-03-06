class BankAccount:
    bank_name="Mojo Dojo"
    balance = 0

    def __init__(self,balance,int_rate):
        self.balance = balance
        self.int_rate = int_rate
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.checkingAccount = BankAccount(int_rate=0.02, balance=0)
        self.savingsAccount = BankAccount(int_rate=0.05, balance=0)

    def deposit(self, amount, string):
        if string == "checking":
            self.checkingAccount.balance+=amount
        elif string == "savings":
            self.savingsAccount.balance+=amount
        else: 
            print("Need to say checking or savings")
        return self

    def withdraw(self, amount):
        self.account.balance-=amount
        return self

    def display_account_info(self):
        print('Balance:' + str(self.checkingAccount.balance))
        return self

    def yield_interest(self):
        if self.account.balance > 0:
            self.account.balance *= (1 + self.account.int_rate)
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
jon = User("Jonathon Smith","jsmith@email.com")

# jon.deposit(500,'checking').withdraw(200).display_account_info().yield_interest().display_account_info()
jon.deposit(500,'checking').display_account_info()