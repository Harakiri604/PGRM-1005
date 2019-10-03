# First we generate a random number, label it as variable "ran_number" and print out what it is
import random
ran_num = random.randint(-10, 150)
print (ran_num)

# Then create a variable "num" that is the remainder of the ran_number divided by 2 
num = ran_num%2

# If ran_number is odd then num will be > 0
if num > 0:
    print ("Not Weird")

# Otherwise it is even and we test for other conditions as per usual
elif ran_num >= 2 and ran_num <= 5:
    print ("Barely Weird")

elif ran_num >= 6 and ran_num <= 20:
    print ("Mildly Weird")

elif ran_num > 20 and ran_num <= 100:
    print ("Super Weird")

elif ran_num <= 0 or ran_num > 100:
    print ("Astronomically Weird")

