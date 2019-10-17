randString="Welcome to the Jungle"

def find(word, char):
    for c in word:
        if c==char:
            return True
    return False

print(find(randString, "W"))



