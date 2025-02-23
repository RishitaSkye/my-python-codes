#__init__() method : it will automatically call at the time of object creation

class Student:
    def __init__(self):       # Special Member Function
        print("Hello!! This is __init__() method")
    def show(self):           # Member Function
        print("Hello!! This is show() method")
ob1= Student()
ob1.show()
#init() method is used to initialize the object