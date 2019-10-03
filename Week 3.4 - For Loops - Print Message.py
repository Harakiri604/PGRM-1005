print("Type in a message to see it 5 times.")
print("Message: ", end="")
text=input()
run=0
for i in range (0,5,1):
    run +=1
    print("%s. %s." % (run, text))
    
