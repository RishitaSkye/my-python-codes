#print(1+5)
#print("apna" + " " +"college")  # concatenation
#print([1,2,3]+[4,5,6]) #merge
#print(type("apna"))

class Complex:

    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")
# Basically its a add function
    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
    
# Basically its a subtraction func
    def __sub__(self,num2):
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return Complex(newReal,newImg)

num1=Complex(3,7)
num1.showNumber()

num2=Complex(5,6)
num2.showNumber()

num3=num1+num2
num3.showNumber()

num3=num1-num2
num3.showNumber()
