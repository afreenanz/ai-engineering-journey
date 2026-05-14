# Build a BankAccount class with the following:
#
# Attributes:
# - owner (string)
# - balance (float, default 0.0)
# - transactions (list, stores history of every deposit/withdrawal)
#
# Methods:
# - deposit(amount): adds amount to balance, records in transactions
#   raises ValueError if amount <= 0
#
# - withdraw(amount): subtracts from balance, records in transactions
#   raises ValueError if amount <= 0
#   raises ValueError if amount > balance (insufficient funds)
#
# - get_history(): prints each transaction with its number
#   Example:
#   1: Deposited 500.0
#   2: Withdrew 200.0
#   3: Deposited 100.0
#
# - __str__: returns "BankAccount(owner=Alice, balance=400.0)"


class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        self.transactions.append(f"Deposited {amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.transactions.append(f"Withdrew {amount:.2f}")

    def get_history(self):
        for i, transaction in enumerate(self.transactions, start=1):
            print(f"{i}: {transaction}")

    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance:.2f})"


if __name__ == "__main__":
    acc = BankAccount("Alice")
    acc.deposit(500)
    acc.withdraw(200)
    acc.deposit(100)
    acc.get_history()
    print(acc)

    # Test error handling
    try:
        acc.withdraw(10000)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        acc.deposit(-50)
    except ValueError as e:
        print(f"Error: {e}")