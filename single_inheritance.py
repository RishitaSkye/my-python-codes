#single inheritance
class Parent:
    def func1(self):
        print("This is parent class")
class Child(Parent):   #Single Inheritance
    def func2(self):
        print("This is child class")
obj=Child()
obj.func1()
obj.func2()     #child class object can access parent class method