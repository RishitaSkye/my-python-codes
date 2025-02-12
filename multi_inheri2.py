class Grandfather:
    grandfathername=" "
    def g(self):
        print(self.grandfathername)
class Father:
    fathername=" "
    def m(self):
        print(self.fathername)
class Son(Grandfather, Father):
    sonname=" "
    def s(self):
        print("Grandfather is: ",self.grandfathername)
        print("Father is: ",self.fathername)
obj=Son()
obj.grandfathername="Raja"
obj.fathername="Suman"
obj.s()