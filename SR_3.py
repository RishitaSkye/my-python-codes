def linear_search(list,key):
 for i in range(len(list)):
    if list[i] == key:
        print(f'Element found at index{i}:')
    else:
        print('Element not found')
list=[]  #empty list
n=int(input('Enter the size of list: '))  #n=6
for i in range (n):  #i=0,1,2,3,4,5
    list.append(input(f'Enter element{i+1}:'))  #This will add all elements in to list
print('The list is:',list) #this will print the list
key=input('Enter an element to search:')
linear_search(list,key) #Method calling
