from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def display_account_type(self):
        pass


class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount >= -5000:
            self._balance -= amount
        else:
            print("Overdraft Limit Reached")

    def display_account_type(self):
        return "Current Account"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Not Enough Balance.")

    def display_account_type(self):
        return "Savings Account"

def print_account_details(account):
    print("Account Number:", account.account_number)
    print("Balance:", account.balance)
    print("Type:", account.display_account_type())
    print("-" * 30)


acc1 = SavingsAccount("SA123", 1000)
acc2 = CurrentAccount("CA456", 1300)

acc1.deposit(200)     
acc2.withdraw(1500)   

print_account_details(acc1)
print_account_details(acc2)
