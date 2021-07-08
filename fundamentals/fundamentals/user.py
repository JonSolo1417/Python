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

    def withdrawal(self,amount):
        self.account_balance-=amount

    def display_user_balance(self):
        print(self.name + ', $' + str(self.account_balance))

    def transfer_money(self,other_user,amount):
        self.account_balance-=amount
        monty.account_balance+=amount
        

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
Jon = User("Jonathon Smith","jsmith@email.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python

guido.deposit(100)
guido.deposit(1000)
guido.deposit(82)
Jon.deposit(200)
Jon.deposit(8000)
monty.deposit(50)

Jon.withdrawal(25)
Jon.withdrawal(200)
guido.withdrawal(200) 
monty.withdrawal(50) 
monty.withdrawal(50) 
monty.withdrawal(50) 

guido.display_user_balance() 
monty.display_user_balance() 
Jon.display_user_balance() 

Jon.transfer_money(monty,500)