import random
maxGuess = input("Guess the number between 1 and: ")
randNum = random.randint(1, int(maxGuess))
counter = 0
userGuess = 0
while (userGuess != randNum):
    userGuess = input("Guess: ")
    counter += 1
    if (int(userGuess) < randNum):
        print("You're too LOW")
    elif (int(userGuess) > randNum):
        print("You're too HIGH")
    else:
        break
print("You guessed it in " + str(counter) + " tries")
