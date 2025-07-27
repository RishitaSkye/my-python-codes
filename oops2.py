#Create Account Class with 2 attributes- balance and account no
#create methods for credit(+ve), debit(-ve), printing and balance

#class-------------------
class Account:

    def __init__(self, bal, acc):
        #attributes--------------
        self.balance=bal
        self.account_no=acc
    
    #methods-----------------
    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount,"Was debited")
        print("total balance=", self.get_balance())
    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount,"Was credited")
        print("total balance=", self.get_balance())
    
    def get_balance(self):
        return self.balance
    
#objects-----------------    
acc1= Account(10000,12345)
acc1.debit(1500)
acc1.credit(550)
acc1.credit(50000)
acc1.debit(1050)