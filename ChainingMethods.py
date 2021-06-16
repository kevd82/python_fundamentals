class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_userBalance(self):
        print(self.name +":", "$" + str(self.account_balance))

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

Kevin = User("Kevin Deming", "barbaricsplendor@gmail.com")
Gina = User("Gina Terkovics", "gina@gmail.com")
Zoey = User("Zoey Katt", "Zoey@gmail.com")

Kevin.make_deposit(122).make_deposit(22).make_deposit(222).display_userBalance()

Gina.make_deposit(322).make_withdrawal(222).make_deposit(100).make_withdrawal(100).display_userBalance()

Zoey.make_deposit(1000).make_withdrawal(200).make_withdrawal(250).make_withdrawal(350).display_userBalance()

Kevin.transfer_money(Zoey, 50).display_userBalance()
Zoey.display_userBalance()
