#choice()
#this function basically takes a sequence as a parameter and returns random values from it
import random
for x in range(3):
 print(random.choice([1,2,6,5,7,4,3,8,9]))

#sample()
print(random.sample([1,2,3,4,5,6,7,8,9],4))