
str1="This is a string"
str2='apna college'
str3="""This is a string\nYou are strong"""
print(str1)
print(str3)

str4="Rishita"
len1=len(str4)
print(len1)
str5="Das"
len2=len(str5)
print(len2)
final_str=str4+" "+str5
print(final_str)

str="apna college"
print(str[2:6])
print(str[4:]) #[4:str(len)]
print(str[:5]) #[0:5]

str="i am a coder."
print(str.capitalize())  #for capital word
print(str.endswith("er."))  #true / false
print(str.replace("coder","girl")) #replace old word with a new word
print(str.find("am"))

#wap to input user's first name and print its length
name=input("enter the first name:")
print(len(name))

#wap to find the occurance of $ in a string
str="$ is a dollar and $ in london $ 34.98"
print(str.count("$"))

light="red"
if(light=="red"):
 print("stop")
elif(light=="green"):
 print("go")
else:
 print("wait")
print("end of the code")
#another question example of conditional statement
marks=int(input("Enter the student marks:")) #marks=56
if(marks>=90):
 Graderade="A" #print("Grade:A")
elif(90>marks>=80):
 grade="B" #print("Grade:B")
elif(80>marks>=70):
 grade="C" #print("Grade:C")
else:
 grade="D" #print("Grade:D")
print("The grade of the student is->", grade)

#wap to check if a number entered by the user is odd or even.
num=int(input("enter the number:"))
if(num%2==0):
  print("The number is even")
else:
  print("The number is odd")

#wap to find the greatest of 3 numbers entered by the user
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if(a>b & a>c):
 print("greatest number is a")
elif(b>c & b>a):
  print("Greatest is b")
else:
  print("greatest is c")

#wap to check if a number is a multiple of 7 or not
num=int(input("enter number:"))
if(num%7==0):
  print("the number is multiple of 7")
else:
  print("not multiple of 7")