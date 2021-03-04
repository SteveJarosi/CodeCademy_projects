class BankAccount:
    balance = 0

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "This account belongs to %s, balance is $%.2f" % (self.name, self.balance)

    def show_balance(self):
        return "Balance is $%.2f" % (self.balance)

    def deposit(self, amount):
        if amount <= 0:
            print "Invalid amount"
            return
        else:
            print "Amount to deposit: $%.2f" % (amount)
            self.balance += amount
            print self.show_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print "Insufficient funds"
            return
        else:
            print "Amount to withdraw: $%.2f" % (amount)
            self.balance -= amount
            print self.show_balance()


my_acc = BankAccount("Jim")
print my_acc
print my_acc.show_balance()
my_acc.deposit(2000)
print my_acc
my_acc.withdraw(1000)
print my_acc
