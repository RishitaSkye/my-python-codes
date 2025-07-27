class Account:
    def __init__(self,acc_no, acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass  #to make password private __ is added

    def reset_pass(self):
        print(self.__acc_pass)

acc1=Account("654258943", "abj$234")
print(acc1.acc_no)
#print(acc1.__acc_pass)
print(acc1.reset_pass())