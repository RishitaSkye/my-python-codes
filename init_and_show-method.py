class Student:            #Always in caps
    department= "EE"       #Public Data Member
    _college= "NSEC"      #Private Data Member

    def __init__(self,roll,name):      #Special Member Function    #Double underscore "__"
        self._roll=roll
        self._name=name
        
    def show(self):                  # Public Member Function
        print("Roll number is:",self._roll)
        print("Name is:",self._name)
#-------------------------------------------------------------------end of class

# creating an object
ob1=Student(1,'Rishita')

# Accessing public data member
print("Department is:",ob1.department)

# Accessing private data member 
print("College is:",ob1._college)

# Calling a method
ob1.show()
