def func(age):
    if (age<0):
        raise ValueError("Age cannot be negative.....")
    else:
        print ("Age is :",age)
try:
    age = int(input("Enter age:"))
    func(age)
except ValueError as neg:
    print(neg)      #e = "Age cannot be negative...""
