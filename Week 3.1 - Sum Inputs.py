print("I will add up the numbers you give me: ", end="")
userinput = float(input())
sum1 = 0

while (userinput != 0):
    sum1 = sum1 + userinput 
    print("Total =  %f" % (sum1))
    print("Let's try the next one: ", end="")
    userinput = float(input())

print("Done!")
