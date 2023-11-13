class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return "Insufficient funds"

class User:
    def __init__(self, initial_balance):
        self.account = BankAccount(initial_balance)

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        return self.account.withdraw(amount)

# Example usage:
user = User(1000)
user.make_deposit(200)
withdrawn_amount = user.make_withdrawal(50)

print(f" user : {user} , Current balance: {user.account.balance}")