import random
answer=random.randint(0, 10)
guess=input("What number am I thinking (between 0 and 10? ")
guess=int(guess)
if(guess==answer):
    print("You got it!")
else:
    print("Sorry, I was actually thinking", answer)
    