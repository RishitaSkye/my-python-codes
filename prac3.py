'''Create a class called Order which stores item & its price.
Use Dunder function __gt__() to convey that
oeder1 > order2 if price of order1 > price of order2'''

class Order:
    def __init__(self,item,price):
        self.item =item
        self.price=price
    
    def __gt__(self,ord2):
        return self.price>ord2.price

ord1=Order("Chips", 10)
ord2=Order("Tea", 56)

print(ord1>ord2)