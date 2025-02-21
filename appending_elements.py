my_tuple=(1,2,3)
my_tuple=my_tuple+(4,5,6) #add elements
print(my_tuple)
t2=(15,12,65,['A','B','V'],87,69,{1:'Rahu', 2:'Ketu'})
print(t2)
print(t2[3][2])
t2[3].pop()
print(t2)
s1={1,2,3,4,5,6}
s2={4,5,6,7,8,9}
print(s1|s2)  #union print(s1.union(s2))
print(s1&s2)
print(s1-s2)
print(s2-s1)
print(s1^s2)
