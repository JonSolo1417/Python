class User:
    # class attributes get defined in the class 
    bank_name = "First National Dojo"
    # now our method has 2 parameters!
    def __init__(self, name, email_address):
    # we assign them accordingly
        self.name = name
        self.email = email_address
        # the account balance is set to $0
        self.account_balance = 0

    def deposit(self,amount):
        self.account_balance+=amount
        return self

    def withdrawal(self,amount):
        self.account_balance-=amount
        return self

    def display_user_balance(self):
        print(self.name + ', $' + str(self.account_balance))
        return self

    def transfer_money(self,other_user,amount):
        self.account_balance-=amount
        monty.account_balance+=amount
        return self
        

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
Jon = User("Jonathon Smith","jsmith@email.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python

guido.deposit(100).deposit(1000).deposit(82).withdrawal(200).display_user_balance() 
Jon.deposit(200).deposit(8000).withdrawal(25).withdrawal(200).transfer_money(monty,500).display_user_balance() 
monty.deposit(50).withdrawal(50).withdrawal(50).withdrawal(50).display_user_balance() 