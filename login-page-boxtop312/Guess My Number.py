import random as r

rand = r.randint(1, 100)
thing = int(input("Guess my number: "))
guessCounter = 0
while thing != rand:
    if thing < rand:
        guessCounter += 1
        print("Too low")
    elif thing > rand:
        guessCounter += 1
        print("Too high")
    thing = int(input("Guess my number: "))
print("You got it!!\nin " + str(guessCounter) + " guesses")
