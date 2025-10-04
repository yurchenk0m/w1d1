class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"The {self.owner}'s bank account"
    
    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += float(amount)
        return self.balance
    
    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= float(amount)
        return self.balance

    def get_balance(self):
        return self.balance
