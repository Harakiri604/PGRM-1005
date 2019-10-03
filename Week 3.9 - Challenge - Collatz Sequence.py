print("Starting number (any positive integer): ", end="")

#this ensures that it is an integer, rather than a float
n=int(input())

#this ensures that it is a positive number
if(n<0):
    print("Let's pretend that you understand what positive means")
    n=n*-1

#create a count to print the starting number only once
count = 0

#create a loop that ends once the sequence reaches number 1
while (n!=1):
    
    #this prints the starting number once and then sets the count to 1, so that the statement is only run once
    if (count == 0):
        print("%.0f" % n, "\t", end="")
        count = 1

    #the final lines check whether n is odd/even and then carries out the relevant calculation before printing the number + inserting a tab + keeping next number on the same line
    elif (n%2==0):
        n=n/2
        print("%.0f" % n, "\t", end="")
    elif (n%2>0):
        n=n*3+1
        print("%.0f" % n, "\t", end="")
        


