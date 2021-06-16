class BankAccount:
    def __init__(self, username, int_rate = 0, balance = 0):
        self.name = username
        self.interest_rate = int_rate
        self.account_balance = balance

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdrawal(self, amount):
        if self.account_balance < amount:
            print("Insufficient funds: $5 fee charged")
            self.account_balance -= 5
        else:
            self.account_balance -= amount
            return self

    def display_account_info(self):
        print(self.name +":", "$" + str(self.account_balance))
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            interest = self.account_balance * self.interest_rate
            self.account_balance = self.account_balance + interest
        return self

Kevin = BankAccount("Kevin Deming", .05, 100)
Gina = BankAccount("Gina Terkovics", .06, 122)

Kevin.deposit(25).deposit(50).deposit(100).withdrawal(25).yield_interest().display_account_info()
Gina.deposit(100).deposit(200).withdrawal(50).withdrawal(50).withdrawal(25).withdrawal(25).yield_interest().display_account_info()