#when a is a number, divisible by b(not zero)
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=a/b
print("a/b= %d"%c)
#other part of the code(after exception):
print("Hi,I am Vikash")


#otherwise when....  a=42, b=0
try:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=a/b
#print("a/b= %d"%c)
#other part of the code(after exception):
except:
  print("can't divide with zero")