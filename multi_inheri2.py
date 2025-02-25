# Multilevel Inheritance
class Grandfather:    #Grandfather
    grandfathername=" "
    def g(self):
        print(self.grandfathername)
class Father(Grandfather):  #Parent Class
    fathername=" "
    def m(self):
        print(self.fathername)
class Son(Grandfather, Father):    #Child of Father
    sonname=" "
    def s(self):
        print("Grandfather is: ",self.grandfathername)
        print("Father is: ",self.fathername)
obj=Son()
obj.grandfathername="Raja"
obj.fathername="Suman"
obj.s()