print("x|", "\t", end="")

for k in range (1,13,1):
    print(str(k), "\t", end="")

print("\n")
print("_"*100)
print("\n")

for i in range (1,13,1):
    print(str(i) + "|", "\t", end="")
    
    for j in range (1,13,1):
        print(i*j, "\t", end="")
    print("\n")
    