class BankAccount:
    interest_rate = 0.005

    def __init__(self, acc_no, balance=0):
        """Initializes instance of BankAccount class"""
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        """Adds the deposit amount to balance"""
        if amount <= 0:
            raise ValueError("Deposit amount should be greater than zero.")
        self.balance += amount

    def withdraw(self, amount):
        """Subracts amount from balance"""
        if amount > self.balance:
            raise ValueError("Withdraw amount cannot be greater than balance.")
        self.balance -= amount


class SavingsAccount(BankAccount):
    interest_rate = 0.03

    def __init__(self, acc_no, balance=5000):
        """Intializes instance of Savings Account"""
        if balance < 5000:
            raise ValueError(
                "Savings Account needs a minimum balance of $5000")
        BankAccount.__init__(self, acc_no, balance)

    def compute_interest(self, no_of_months=0):
        """Computes the interest for specified number of months on a given monthly rate"""
        return self.balance * (1 + SavingsAccount.interest_rate)**no_of_months


class CheckingAccount(BankAccount):
    pass
