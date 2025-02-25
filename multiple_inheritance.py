class Father:
    fathername=" "
    def f(self):
        print(self.fathername)
class Mother:
    mothername=" "
    def m(self):
        print(self.mothername)
class Son(Father, Mother):   #child of father and mother class
    sonname=" "
    def s(self):
        print("Father is: ",self.fathername)
        print("Mother is: ",self.mothername)
obj=Son()
obj.fathername="Ram"
obj.mothername="Sita"
obj.s()