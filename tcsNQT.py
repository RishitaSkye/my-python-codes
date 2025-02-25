n=int(input())
j=0
arr=[0 for i in range(n)]
for i in range(n):
    a=int(input())
    if a!=0:
        arr[j]=a
        j+=1
for i in arr:
    print(i,end="")
