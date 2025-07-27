class Student:
    def __init__(self, phys, chem, math):
        self.phys=phys
        self.chem=chem
        self.math=math
        # percentage
        #self.percentage=str ((self.phys+self.chem+self.math)/3) +"%"

    #def calcPercentage(self):
      #  self.percentage=str ((self.phys+self.chem+self.math)/3) +"%"

    @property
    def percentage(self):
        return str((self.phys+self.chem+self.math)/3) +"%"
stu1=Student(98,69,75)
print(stu1.percentage)

stu1.phys=90
print(stu1.phys)
print(stu1.percentage)   # willnot change,same as before
#stu1.calcPercentage()
#print(stu1.percentage)