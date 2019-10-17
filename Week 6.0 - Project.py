#Import libraries
import random
import time

#Define global variables
deck=[2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]
user_hand = 0
dealer_hand = 0


#Create functions to draw a card + add to the hand + remove it from the deck for user 
def user_draw():
    global user_hand
    draw = random.choice(deck)
    user_hand += draw
    deck.remove(draw)
    return draw

#And the same function for dealer
def dealer_draw():
    global dealer_hand
    draw = random.choice(deck)
    dealer_hand += draw
    deck.remove(draw)
    return draw

#Print welcome message
print("Welcome to the Awesome Blackjack(ish) Program!")
print("")
time.sleep(1)

#Deal out the user's initial cards
latest_draw = user_draw()
print("Your first card is valued at: " + str(latest_draw))
time.sleep(1)
latest_draw = user_draw()
print("Your second card is valued at: " + str(latest_draw))
time.sleep(1)
print("Your total is currently: " + str(user_hand))
print("")
time.sleep(1)

#And the dealer's card
latest_draw = dealer_draw()
print("One of the dealer's cards is valued at: " + str(latest_draw))
latest_draw = dealer_draw()
print("")

#Then create a loop that checks whether the user hand is below 21 and then gives them the choice to draw another if so
another_draw = True
while user_hand < 21 and another_draw == True:
    print ("Would you like to draw another card? (y/n): ", end="")
    prompt = input()
    if prompt == "y" or prompt == "Y":
        latest_draw=user_draw()
        print("Your latest draw is: " + str(latest_draw))
        print("Your total is: " + str(user_hand))
        time.sleep(1)

    elif prompt == "n" or prompt == "N":
        another_draw = False
        print("Now let's see how lucky the dealer is.")
        print("")
        time.sleep(1)

#Then print a message in case they are bust or hit 21
if user_hand > 21:
    print("You are bust!")

elif user_hand == 21:
    print("You have reached the target score!")
    print("Now let's see if the dealer is just as lucky")

#Run the dealer's draw until dealer's hand reaches 16 or above (subject to the user score being at or below 21) and then compare results
if user_hand <= 21:
    
    while dealer_hand <= 16:
        latest_draw=dealer_draw()
        print("The dealer drew a card that is worth " + str(latest_draw))
        print("The dealer's total is " + str(dealer_hand))
        time.sleep(1)

    if dealer_hand > 21:
        print("The dealer's total is " + str(dealer_hand))
        print("You win!")
        time.sleep(1)
  
    elif user_hand > dealer_hand:
        print("The dealer's total is " + str(dealer_hand))
        print("You win!")
        time.sleep(1)

    elif user_hand == dealer_hand:
        print("The dealer's total is " + str(dealer_hand))
        print("It's a draw!")
        time.sleep(1)

    else:
        print("The dealer's total is " + str(dealer_hand))
        print("You lose!")
        time.sleep(1)
 





