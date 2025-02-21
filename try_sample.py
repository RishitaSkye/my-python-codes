a=int(input("Enter a:"))
b=int(input("Enter b:"))
try:   #try block contains thr block of code that causes exception
    c=a/b
except:   #call when try block found exception
    print("Can't divide with zero")
else:   #Else block will print when there is no exception in try block
    print("Result is:",c)
    print("This is else block")
finally:    #It will execute in all the cases
    print("This is finally block")