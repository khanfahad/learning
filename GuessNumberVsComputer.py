import random
def returnHalf(minNum, maxNum):
    rangeNum = int((maxNum - minNum)/2)
    return int(rangeNum + minNum)

def systemGuess(maxGuess, randNum):
    minNum = 0
    sysCounter = 0
    sysGuess = 0
    maxNum = maxGuess
    while (sysGuess != randNum):
        sysGuess = int(returnHalf(minNum,maxNum))
        sysCounter += 1
        if (int(sysGuess) < randNum):
            minNum = sysGuess
        elif (int(sysGuess) > randNum):
            maxNum = sysGuess
        else:
            break
    return sysCounter

maxGuess = input("Guess the number between 1 and: ")
randNum = random.randint(1, int(maxGuess))
sysCounter = systemGuess(int(maxGuess), randNum)

userCounter = 0
userGuess = 0
while (userGuess != randNum):
    userGuess = input("Guess: ")
    userCounter += 1
    if (int(userGuess) < randNum):
        print("You're too LOW")
    elif (int(userGuess) > randNum):
        print("You're too HIGH")
    else:
        break
print("You guessed it in " + str(userCounter) + " tries.")
print("It took the system " + str(sysCounter) + " tries.")
