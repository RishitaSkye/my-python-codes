'''
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
odd_list=[i for i in list if i%2!=0]
even_list=[i for i in list if i%2==0]
print("ODD_LIST----")
print(odd_list)
print("EVEN_LIST----")
print(even_list)
sum_odd=sum(odd_list)
mul=1
for i in even_list:
    mul=mul*i

print("Sum of odd_list: ",sum_odd)
print("Multiplication of even_list: ",mul)

#dictionary
d={1:'Ram', 2:'Sita'}  #key-value
print(d)
d1=dict(a="Nil", b="Sira", c="woh")
print(d1)
d[4]='Sumon' #Adding and updating the dict
print(d)
#keys should be unique but values may be duplicate
del d[4]
print(d)
d={1:'Ram', 2:'Sita', 3:'Ritwick'}
print(d.get(2))
print(d.get('Laxman'))
'''
'''
rows=int(input("Enter the number of rows: "))
column=int(input("Enter the number of columns: "))
print("Enter the elements of first matrix:")
matrix_a=[[int(input())for i in range(column)]for i in range(rows)]
print("First matrix is:")
for i in matrix_a:
    print(i)
print("Enter the elements of second matrix:")
matrix_b=[[int(input())for i in range(column)]for i in range(rows)]
for i in matrix_b:
    print(i)
result=[[0 for i in range(column)]for i in range(rows)]
for i in range(rows):
    for j in range(column):
        result[i][j]=matrix_a[i][j]+matrix_b[i][j]
print("The sum of above two matrices is:")
for i in result:
    print(i)
'''
'''
import random
for x in range(2):
 print(random.randint(2,9))
 
import random
for x in range(5):
 print(random.randrange(2,60,2))
 
import random
for x in range(15):
 print(random.random())

import random
for x in range(5):
 print(random.uniform(2,7))
 
for x in range(3):
 print(random.choice([1,2,3,4,5,6,7,8,9]))
 print(random.sample([1,2,3,4,5,6,7,8,9],4))
 '''
a=int(input("Enter a:"))
b=int(input("Enter b:"))
print("Welcome")
c=a/b #zero division error: division by zero
print("Division is ",c)
print("Thank you")