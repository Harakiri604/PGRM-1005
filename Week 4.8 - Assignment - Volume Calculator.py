#First we import the necessary libraries
import time
import math

#Then define the math functions
def cub_vol():
    print("Input one of the cube's lengths: ", end="")
    cubL = float(input())
    volume = cubL**3
    return volume
    
def pri_vol():
    print("Input the first length: ", end="")
    priL1 = float(input())
    print("Input the second length: ", end="")
    priL2 = float(input())
    print("Input the third length: ", end="")
    priL3 = float(input())
    volume = priL1*priL2*priL3
    return volume

def cyl_vol():
    print("Input the radius: ", end="")
    cylR = float(input())
    print("Input the height: ", end="")
    cylH = float(input())
    volume = cylR**2*math.pi*cylH
    return volume

def pyr_vol():
    print("Input the width: ", end="")
    pyrW = float(input())
    print("Input the length: ", end="")
    pyrL = float(input())
    print("Input the height: ", end="")
    pyrH = float(input())
    volume = 1/3*pyrW*pyrL*pyrH
    return volume

def con_vol():
    print("Input the radius: ", end="")
    conR = float(input())
    print("Input the height: ", end="")
    conH = float(input())
    volume = 1/3*conR**2*math.pi*conH
    return volume

def sph_vol():
    print("Input the radius: ", end="")
    sphR = float(input())
    volume = 4/3*sphR**3*math.pi
    return volume

#And a "menu" function
def get_menu():
    print("Menu:")
    print("1. Calculate the volume of a cube")
    print("2. Calculate the volume of a rectangular prism")
    print("3. Calculate the volume of a cylinder")
    print("4. Calculate the volume of a pyramid")
    print("5. Calculate the volume of a cone")
    print("6. Calculate the volume of a sphere")
    print("7. Get me outta here")
    print("Please chose one of the above options by typing in its number (e.g. 1): ", end="")
    prompt=input()
    return prompt

#Print an intro message once
print("Welcome to the Awesome Volume Calculator, specifically designed for those who are too lazy to use a calculator.")
time.sleep(1)
print()

#Get the options menu and user input
while True:
    prompt = int(get_menu())
    if prompt == 1:
        print("The volume is: " + str(cub_vol()))
        time.sleep(1)
    elif prompt == 2:
        print("The volume is: " + str(pri_vol()))
        time.sleep(1)
    elif prompt == 3:
        print("The volume is: " + str(cyl_vol()))
        time.sleep(1)
    elif prompt == 4:
        print("The volume is: " + str(pyr_vol()))
        time.sleep(1)
    elif prompt == 5:
        print("The volume is: " + str(con_vol()))
        time.sleep(1)
    elif prompt == 6:
        print("The volume is: " + str(sph_vol()))
        time.sleep(1)
    elif prompt == 7:
        break

print("Thanks and goodbye!")
