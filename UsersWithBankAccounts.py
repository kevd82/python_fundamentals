class BankAccount:
    def __init__(self, int_rate = 0, balance = 0):
        self.interest_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if self.balance < amount:
            print("Insufficient funds: $5 fee charged")
            self.balance -= 5
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print("Account Balance:", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.interest_rate
            self.balance = self.balance + interest
        return self

class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(0.01)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdrawal(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

    def yieldInterest(self):
        self.account.yield_interest()
        return self
        

Kevin = User("Kevin Deming", "Kevin@gmail.com")

Kevin.make_deposit(122).make_deposit(144).make_withdrawal(44).yieldInterest().display_user_balance()