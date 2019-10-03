#We start with the intro message and a time delay to give the user a chance to read
print ("Tremble mortal, for you are in the presence of the awesomeness that is this quiz!")
import time
time.sleep(2)
print ("Are you ready to begin?")

#Then give them an illusion of free will with a looping prompt
while True:
    prompt = input()
    if prompt == ("Yes") or prompt == ("yes") or prompt == ("Y") or prompt == ("y"):
        print ("So eager... you must be smarter than you look")
        break
    else:
        print ("Hmmmmmm... let's try again... are you ready to begin?")

#No reason for below
time.sleep(2)
print ("Let's begin the test then...")
time.sleep(2)

#Now on to the test. First, we create a "score" variable and set it to 0
score = 0

#Then ask the first question
print ("First question...")
time.sleep(2)
print ("Q1) What is the airspeed velocity of an unladen Swallow? \n \t 1. 7 mph \n \t 2. 24 mph \n \t 3. What do you mean? African or European swallow?")

#Here we create a variable that is their answer, then use a loop to ensure that they can only chose one of three options, then increase the score by 0, 1 or 2 depending on their choice
while True:
    answer1 = input()
    if answer1 == ("1") or answer1 == ("1."):
        score = score
        break
    elif answer1 == ("2") or answer1 == ("2."):
        score = score + 1 
        break
    elif answer1 == ("3") or answer1 == ("3."):
        score = score + 2
        break
    else:
        print ("Nevermind, I guess you are exactly as smart as you look... shall we try again?")

#Rinse and repeat
print("Alright, next question...")
time.sleep(2)
print("Q2) How much wood would a woodchuck chuck if a woodchuck could chuck wood? \n \t 1. All the wood \n \t 2. Some of the wood \n \t 3. None of the wood")
while True:
    answer2 = input()
    if answer2 == ("1") or answer2 == ("1."):
        score = score + 2
        break
    elif answer2 == ("2") or answer2 == ("2."):
        score = score + 0 
        break
    elif answer2 == ("3") or answer2 == ("3."):
        score = score + 0
        break
    else:
        print ("Aaaaaaaaahhh mortals these days, it really is not that hard... just put in 1 or 2 or 3... or did you never play tonque twisters as a kid?")

#Rinse and repeat 
print("And finally...")
time.sleep(2)
print ("Q3) Does the pope $#1t in the woods? \n \t 1. What's with you and the wood? \n \t 2. Does the bear? \n \t 3. Yes")
while True:
    answer3 = input()
    if answer3 == ("1") or answer3 == ("1."):
        score = score + 2
        break
    elif answer3 == ("2") or answer3 == ("2."):
        score = score + 0 
        break
    elif answer3 == ("3") or answer3 == ("3."):
        score = score + 1
        break
    else:
        print ("I need a new line of work... try again")

#Finally, spit out the number
time.sleep(1)
print("Congratulations, your total score is", score)
