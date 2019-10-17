randArray=[]

import random

for i in range (100):
    randArray.append(random.randint(1,1000))

print(randArray)

randArray.sort()

print(randArray)
