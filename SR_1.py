prices=[238,58,65,45,21,14,78,69,96,81]
print(prices)
list1=[1,36.6,'Hello',7,14.38]
print(list1)
print(type(prices))
print(type(list1))
prices.sort()
print(prices)
prices.sort(reverse=True)  #Decending order
print(prices)
months=['January', 'February', 'March', 'April']
print(months)
months.append('May')  #It will add the element at the end
print(months)
months.extend(['June','July','August'])
print(months)
months.insert(1,'December')  #Add the element in a specific index
print(months)
months.remove('December')
print(months)

list2=[10,23,54,59,457,36,45,98,74,48,84,31,24,56]
print(max(list2))
print(min(list2))
print(len(list2))
list1=['India','Germany',251,4000,'Australia',5487]
list2=[4000,5200,6542,1200,3298,4514]
list3=["Yellow","Blue","Green","Red"]
print("len :\t\t", len(list1)) #this function returns the total length of the list
print("max [integer]:\t",max(list3)) 
# max : This function returns the item from list have largest value
#max not works for list1 it will throw typeerror
print("max[string]:\t", max(list2))  #check first alphabet only
#min : This function returns the item from list have smallest value only.
print("min [integer]:\t",min(list3))
print("min [string]:\t",min(list2))
list1.append('Japan')
print("append: ",list1)
list1.insert(3,'China')
print("insert: ",list1)
list1.insert(0,'pakistan')
#reverse: this function reverses items of list in place
list1.reverse()
print("reverse:",list1)
#count: this function returns count of how manytimes item exist in the first
print("count:",list1.count('Pakistan'))
print("count:",list1.count('Pakistan'))
print("count:",list1.count(4000))
print("count:",list1.count('4000'))
#index: this function appends one list to another
#if item not found in list it will throw valueerror
print("index: ", list1.index(4000))
print("index: ", list3.index("Red"))
print("index: ",list3.index("Yellow"))
#pop:  this function removes and returns last item from list
list1.pop()
print("pop: ",list1)
list1.pop()
print("pop:",list1)
list2=[10,20,30,40,50,5,12,15,99]
print(max(list2))
print(min(list2))
print(len(list2))
print(list2.count(15))
list2.pop()
print(list2)
del(list2[2])
