d={1:'Ram',2:'Sita',3:'Laxman'}
print (d)
print(d[1]) 
d[4]='Suman' #adding and updating the dictionary
print(d) #keys shouldbe unique but values maybe duplication
d={1:'Ram',2:'Sita',3:'Laxman'}
for i in d:
    print(i)
print("-------------------------")
for i in d.values():
    print(i)
d={1:'Ram',2:'Sita',3:'Laxman'}
for i,j in d.items():
    print(i,j)
d={1:'Ram',2:'Sita',3:'Laxman'}
print(d.get(2))
key=next((i for i,j in d.items()if j=='Laxman'),None)
print(key)

d1={1:'A', 2:'B'}
d2={2:'C', 3:'D'}
d1.update(d2)  #Merge two dictionaries but unique value
print(d1)
# same as
d3=d1|d2  
print(d3)