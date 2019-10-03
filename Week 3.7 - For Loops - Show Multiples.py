print("Chose a number: ", end="")
text=int(input())

for i in range (1,13):
    print("%sx%s =" % (text,i), text*i)
