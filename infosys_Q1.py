#Base/Parent class vehicle
class Vehicle:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display_info(self):
        print(self.brand)
        print(self.model)
        print(self.year)
#Derived/Child class Car
class Car(Vehicle):
    def __init__(self,brand,model,year,num_doors):
        super().__init__(brand,model,year)
        self.num_doors=num_doors
    def display_info(self):
        super().display_info()
        print(self.num_doors)
#Child class Motorcycle
class Motorcycle(Vehicle):
    def __init__(self,brand,model,year,engine_capacity):
        super().__init__(brand,model,year)
        self.engine_capacity=engine_capacity
    def display_info(self):
        super().display_info()
        print(self.engine_capacity)
#Demonstration
c1=Car("Toyota", "Innova", 2023,4)
m1=Motorcycle("Yamaha", "R15",2024, "160cc")

print("******CAR DETAILS******")
c1.display_info()
print("******MOTORCYCLE DETAILS******")
m1.display_info()