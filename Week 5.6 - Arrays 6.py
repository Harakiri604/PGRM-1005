randString="Welcome to the Jungle"

def index(word, char):
    for index, value in enumerate(word):
        if value==char:
            return index
    return -1

print(index(randString, "J"))



