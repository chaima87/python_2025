class BankAccount:
    def __init__(self, balance=0, interest_rate=0.01):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        """Deposits money into the bank account."""
        self.balance += amount

    def withdraw(self, amount):
        """Withdraws money from the bank account."""
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def yield_interest(self):
        """Applies interest to the balance."""
        self.balance += self.balance * self.interest_rate

    def display_account_info(self):
        """Displays the balance of the account."""
        print(f"Balance: ${self.balance:.2f}")

class User:
    def __init__(self, name, balance=0, interest_rate=0.01):
        self.name = name
        self.account = BankAccount(balance, interest_rate)  
        
    def make_deposit(self, amount):
        """Calls the deposit method of the associated BankAccount."""
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        """Calls the withdraw method of the associated BankAccount."""
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        """Displays the user's account balance."""
        print(f"User: {self.name}, ", end="")
        self.account.display_account_info()
        return self

    def yield_interest(self):
        """Applies interest to the user's bank account."""
        self.account.yield_interest()
        return self

# Creating users with associated bank accounts
user1 = User("Michael", 300, 0.02)  # Starts with $300, 2% interest
user2 = User("John", 500, 0.05)    # Starts with $500, 5% interest

# Chained operations for user1
user1.make_deposit(50).make_deposit(100).make_withdrawal(75).yield_interest().display_user_balance()

# Chained operations for user2
user2.make_deposit(200).make_withdrawal(150).make_withdrawal(100).yield_interest().display_user_balance()

class User:
    def __init__(self, name):
        self.name = name
        self.accounts = {}  # Dictionary to store multiple bank accounts
        self.default_account = None  # Default account name for easy transactions

    def open_account(self, account_name, balance=0, interest_rate=0.01):
        """Creates a new BankAccount and associates it with this user."""
        self.accounts[account_name] = BankAccount(balance, interest_rate)
        if not self.default_account:  # Set the first account as the default
            self.default_account = account_name
        print(f"{self.name} opened a new account: '{account_name}' with balance ${balance}")
        return self

    def set_default_account(self, account_name):
        """Sets the default account for transactions if no account is specified."""
        if account_name in self.accounts:
            self.default_account = account_name
            print(f"{self.name}'s default account is now '{account_name}'.")
        else:
            print(f"Account '{account_name}' does not exist.")
        return self

    def make_deposit(self, amount, account_name=None):
        """Deposits money into the specified account or default account."""
        account_name = account_name or self.default_account
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
            print(f"{self.name} deposited ${amount} into '{account_name}'.")
        else:
            print(f"Account '{account_name}' not found.")
        return self

    def make_withdrawal(self, amount, account_name=None):
        """Withdraws money from the specified account or default account."""
        account_name = account_name or self.default_account
        if account_name in self.accounts:
            self.accounts[account_name].withdraw(amount)
            print(f"{self.name} withdrew ${amount} from '{account_name}'.")
        else:
            print(f"Account '{account_name}' not found.")
        return self

    def yield_interest(self, account_name=None):
        """Applies interest to the specified account or default account."""
        account_name = account_name or self.default_account
        if account_name in self.accounts:
            self.accounts[account_name].yield_interest()
            print(f"Interest applied to '{account_name}' for {self.name}.")
        else:
            print(f"Account '{account_name}' not found.")
        return self

    def display_user_balance(self, account_name=None):
        """Displays the balance of a specific account or all accounts."""
        if account_name:
            if account_name in self.accounts:
                print(f"User: {self.name}, Account: '{account_name}', ", end="")
                self.accounts[account_name].display_account_info()
            else:
                print(f"Account '{account_name}' not found.")
        else:
            print(f"\n--- {self.name}'s Accounts ---")
            for acc_name, acc in self.accounts.items():
                print(f"Account: '{acc_name}', ", end="")
                acc.display_account_info()
            print("----------------------------\n")
        return self
    
    def transfer_money(self, amount, other_user, account_name=None):
        """Transfers money from this user's account to another user's account."""
        account_name = account_name or self.default_account
        if account_name in self.accounts:
            # Withdraw from this user's account
            if self.accounts[account_name].balance >= amount:
                self.accounts[account_name].withdraw(amount)
                print(f"{self.name} withdrew ${amount} from '{account_name}' for transfer.")
                # Deposit into the other user's account
                other_user.make_deposit(amount, other_user.default_account)
                print(f"{self.name} transferred ${amount} to {other_user.name}'s account.")
            else:
                print(f"Insufficient funds in {self.name}'s '{account_name}' account.")
        else:
            print(f"Account '{account_name}' not found.")
        return self
    
# Creating a user with multiple accounts
user1 = User("Michael")

# Opening multiple accounts
user1.open_account("Checking", 500, 0.02).open_account("Savings", 1000, 0.05)

# Set a default account
user1.set_default_account("Checking")

# Making deposits and withdrawals (specifying accounts)
user1.make_deposit(200, "Checking").make_deposit(500, "Savings")
user1.make_withdrawal(100, "Checking").make_withdrawal(50, "Savings")

# Yielding interest (default is "Checking", unless specified)
user1.yield_interest("Savings").yield_interest()

# Displaying balances
user1.display_user_balance()  
user1.display_user_balance("Checking") 

# Creating users with multiple accounts
user1 = User("Michael")
user2 = User("John")

# Opening multiple accounts for both users
user1.open_account("Checking", 500, 0.02).open_account("Savings", 1000, 0.05)
user2.open_account("Checking", 200, 0.01).open_account("Savings", 1500, 0.03)

# Setting default accounts
user1.set_default_account("Checking")
user2.set_default_account("Savings")

# Transferring money from Michael to John
user1.transfer_money(200, user2)

# Displaying updated balances for both users
user1.display_user_balance()  # Michael's balances
user2.display_user_balance()  # John's balances
