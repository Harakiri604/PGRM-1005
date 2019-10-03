weight=input("How much do you weigh: ")
weight=float(weight)

print("I have information for the following planets: 1. Venus 2. Mars 3. Jupiter 4. Saturn 5. Uranus 6. Neptune")
planet=input("Which planet do you want to visit: ")
planet=int(planet)

if(planet == 1):
    relative_weight=weight*0.78
    print("Your weight on Venus is", relative_weight)
elif(planet == 2):
    relative_weight=weight*0.39
    print("Your weight on Mars is", relative_weight)
elif(planet == 3):
    relative_weight=weight*2.65
    print("Your weight on Jupiter is", relative_weight)
elif(planet == 4):
    relative_weight=weight*1.17
    print("Your weight on Saturn is", relative_weight)
elif(planet == 5):
    relative_weight=weight*1.05
    print("Your weight on Uranus is", relative_weight)
elif(planet == 6):
    relative_weight=weight*1.23
    print("Your weight on Neptune is", relative_weight)
else:
    print("Error")
