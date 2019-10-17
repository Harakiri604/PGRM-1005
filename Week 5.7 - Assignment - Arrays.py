#Let's import what we need first
import random
import time

#Then declare the array as a global variable and populate it initially in case the user first chooses an option other than to create a new array
user_array=[]
for i in range (20):
    user_array.append(random.randint(1,100))

#Create a menu function
def get_menu():
    print("What would you like to do?\n")
    print("1) Create a new integer array")
    print("2) Find the max value")
    print("3) Find the min value")
    print("4) Find the average value")
    print("5) Find the index of a value")
    print("6) See if a number is in the array")
    print("7) Find the # of occurances of a value")
    print("8) Print out the array")
    print("9) Get me outta here!\n")
    prompt = int(input("Input the number of your chosen option: "))
    return prompt

#Define the functions to cover all the options except for option 8 (seems like an overkill to define a function that just prints the array)
def new_array(array_size):
    user_array.clear()
    for i in range (array_size):
        user_array.append(random.randint(1,100))

def max_array():
    return max(user_array)

def min_array():
    return min(user_array)

def average_array():
     return sum(user_array)/len(user_array)

def index_array(user_array, target_value):
    for index, value in enumerate(user_array):
        if value == target_value:
            return index
    return -1

def value_array(user_array, target_value):
    for index, value in enumerate(user_array):
        if value == target_value:
            return True
    return False

def occur_array(user_array, target_value):
    instances = 0
    instances = int(instances)
    for index, value in enumerate(user_array):
        if value == target_value:
            instances += 1
    return instances

#And put it all in a loop
while True:
    prompt = int(get_menu())
    if prompt == 1:
        print("Enter the size of the new array: ", end="")
        array_size = input()
        array_size = int(array_size)
        new_array(array_size)
        print("A new array has been created.\n")
        time.sleep(1)
    
    elif prompt == 2:
        print("The maximum value in the array is: ", end="")
        print(max_array())
        print("")
        time.sleep(1)

    elif prompt == 3:
        print("The minimum value in the array is: ", end="")
        print(min_array())
        print("")
        time.sleep(1)
    
    elif prompt == 4:
        print("The average value in the array is: ", end="")
        print(average_array())
        print("")
        time.sleep(1)
    
    elif prompt == 5:
        print("Enter the value you wish to find the index for: ", end="")
        target_value = input()
        target_value = int(target_value)
        if index_array(user_array, target_value) != -1:
            print("The index of the target value is: ", end="")
            print(index_array(user_array, target_value))
            print("")
        else:
            print("The value was not found\n")
        time.sleep(1)
    
    elif prompt == 6:
        print("Enter the value you wish to check: ", end="")
        target_value = input()
        target_value = int(target_value)
        print("Has the value been found (True or False): ", end="")
        print(value_array(user_array, target_value))
        print("")
        time.sleep(1)
    
    elif prompt == 7:
        print("Enter the value you wish to check: ", end="")
        target_value = input()
        target_value = int(target_value)
        print("There number of times this value appears in the array is: ", end="")
        print(occur_array(user_array,target_value))
        print("")
        time.sleep(1)

    elif prompt == 8:
        print("The array is as follows: ", end="")
        print(user_array)
        print("")
        time.sleep(1)

    elif prompt == 9:
        break

print("Thanks and goodbye!")

