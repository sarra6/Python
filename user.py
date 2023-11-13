class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds for withdrawal.")

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")

    def transfer_money(self, other_user, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_user.balance += amount
        else:
            print("Insufficient funds for the transfer.")

# Example usage:
user1 = User("Guido van Rossum", 150)
user2 = User("Larry Page", 200)

user1.make_withdrawal(50)
user1.display_user_balance()

user1.transfer_money(user2, 30)

user1.display_user_balance()
user2.display_user_balance()
