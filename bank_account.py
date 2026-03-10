class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        print("Balance:", self.balance)


a = BankAccount(101, 5000)
a.deposit(1000)
a.withdraw(500)
a.check_balance()