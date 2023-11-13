class BankAccount:
    def __init__(self, balance=0, interest_rate=0.01):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Insufficient funds: Charging a $5 fee")
                self.balance -= 5
        else:
            print("Invalid withdrawal amount. Please withdraw a positive amount.")

    def display_account_info(self):
        print(f"Balance: ${self.balance:.2f}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate

# Example usage:
account1 = BankAccount(1000, 0.02)  # Create an account with a $1000 balance and a 2% interest rate

account1.display_account_info()  
account1.deposit(500) 
account1.display_account_info()  

account1.withdraw(200) 
account1.display_account_info() 

account1.yield_interest() 
account1.display_account_info()  
