class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self  # Return self to allow method chaining

    def make_withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        return self  # Return self to allow method chaining

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")
        return self  # Return self to allow method chaining

    def transfer_money(self, other_user, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            other_user.balance += amount
        return self  # Return self to allow method chaining

# Example usage with method chaining:
user1 = User("Guido van Rossum", 150)
user2 = User("Larry Page", 200)

user1.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()

user2.make_deposit(50).make_deposit(75).make_withdrawal(25).display_user_balance()

# Transferring money with method chaining:
user1.transfer_money(user2, 40).display_user_balance()
user2.display_user_balance()
