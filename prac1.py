'''Define a circle to create a circle with radius r using the constructor.
Define an Area() method of the class which calculates the area of the circle.
Define a perimeter() method of the class which allowsyou to calculate the perimeter of the circle.'''

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def Area(self):
        return 3.14 * self.radius ** 2
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1=Circle(21)
print(c1.Area())
print(c1.perimeter())