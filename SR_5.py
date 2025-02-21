list =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
odd_list=[i for i in list if i%2 !=0]
even_list=[i for i in list if i%2 ==0]
print("Odd list.....")
print(odd_list)
print("Even list.....")
print(even_list)
sum_odd=sum(odd_list)
mul=1
for i in even_list:
    mul*=i
print("Sum of odd list:",sum_odd)
print("Multiplication of even_list:",mul)