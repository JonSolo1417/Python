class BankAccount:
    bank_name="Mojo Dojo"
    int_rate = .01
    balance = 0

    def __init__(self):  
        pass

    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        self.balance-=amount
        return self

    def display_account_info(self):
        print('Balance:' + str(self.balance))

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.int_rate)
        return self

    @classmethod
    def change_int_rate(cls,new_rate):
        cls.int_rate=new_rate


a = BankAccount()
a.int_rate=.03
a.balance=100
b = BankAccount()

a.deposit(500).deposit(200).deposit(300).withdraw(900).yield_interest().display_account_info()
b.deposit(500).deposit(200).withdraw(300).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

BankAccount.change_int_rate(.05)

c = BankAccount()

print(c.int_rate)