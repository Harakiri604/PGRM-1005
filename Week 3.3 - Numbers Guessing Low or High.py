import random
answer=random.randint(1, 100)
guess=input("What number am I thinking (between 1 and 100)? You have 7 guesses: ", end="")
guess=int(guess)
counter = 0

while (counter <6)
if(guess==answer):
    print("You got it!")
else:
    print("Sorry, I was actually thinking", answer)
    
