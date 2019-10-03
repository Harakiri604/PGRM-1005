weight=input("How much do you weigh: ")
weight=float(weight)

print("I have information for the following planets: 1. Venus 2. Mars 3. Jupiter 4. Saturn 5. Uranus 6. Neptune")
planet=input("Which planet do you want to visit: ")

if(planet == "Venus" or planet == "venus"):
    relative_weight=weight*0.78
    print("Your weight on Venus is", relative_weight)
    
elif(planet == "Mars" or planet == "mars"):
    relative_weight=weight*0.39
    print("Your weight on Mars is", relative_weight)
    
elif(planet == "Jupiter" or planet =="jupiter"):
    relative_weight=weight*2.65
    print("Your weight on Jupiter is", relative_weight)
    
elif(planet == "Saturn" or planet == "saturn"):
    relative_weight=weight*1.17
    print("Your weight on Saturn is", relative_weight)
    
elif(planet == "Uranus" or planet == "uranus"):
    relative_weight=weight*1.05
    print("Your weight on Uranus is", relative_weight)
    
elif(planet == "Neptune" or planet == "neptune"):
    relative_weight=weight*1.23
    print("Your weight on Neptune is", relative_weight)
    
else:
    print("Error")
