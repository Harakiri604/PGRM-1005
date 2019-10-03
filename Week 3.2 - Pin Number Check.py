print("Please enter your 4 digit pin: ", end="")
pin = int(input())
counter = 0

while (counter < 2):
    if (pin != 1234):
        counter += 1
        print("Please try again: ", end="")
        pin = int(input())
    elif (pin == 1234):
        print("Correct!")
        break
       
if (counter == 2):
    print("You got locked out!")
