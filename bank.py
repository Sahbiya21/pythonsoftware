class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount} into {self.name}'s account.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount} from {self.name}'s account.")

    def check_balance(self):
        print(f"{self.name}'s balance: ${self.balance}")

# Create a bank account
account = BankAccount("John", 1000)

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(200)

# Check balance
account.check_balance()
