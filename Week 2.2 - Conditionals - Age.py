name=input("What is your name: ")
age=input("How old are you: ")
age=float(age)
age=int(age)
if(age < 16):
    print("You can't drive",name)
elif(age >= 16 and age <= 17):
    print("You can drive but not vote",name)
elif(age >=18 and age <= 24):
    print("You can vote but not rent a car",name)
else:
    print("You",name,"are the king of the world!")
