class Person:
    __name="anonymous"

    def __hello(self):
        print("hello, person!")
    def welcome(self):
        self.__hello()
p1=Person()
print(p1.welcome())




#MultiLevel Inheritance
class Car:

    @staticmethod
    def Start():
        print("Car started..")
    @staticmethod
    def Stop():
        print("Car stopped..") 

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type
car1=Fortuner("disel")
car1.Start()
