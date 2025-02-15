class BankAccount:
    accounts = []
    def __init__(self, balance=0, interest_rate=0.01):
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        """Increases the balance by the given amount."""
        self.balance += amount
        return self 

    def withdraw(self, amount):
        """Decreases the balance by the given amount, checking for sufficient funds."""
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        """Prints the account balance."""
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        """Increases the balance by the current balance * interest rate if the balance is positive."""
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        return self 
    
    @classmethod
    def print_all_accounts(cls):
        """Prints the account info for all instances of BankAccount."""
        print("\n--- All Bank Accounts Info ---")
        for account in cls.accounts:
            account.display_account_info()
        print("------------------------------\n")

account1 = BankAccount(200, 0.03)
account1.deposit(50).deposit(25).deposit(75).withdraw(100).yield_interest().display_account_info()

account2 = BankAccount(500, 0.05)
account2.deposit(100).deposit(50).withdraw(200).withdraw(50).withdraw(100).withdraw(400).yield_interest().display_account_info()

BankAccount.print_all_accounts()