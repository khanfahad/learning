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
    print("Sys counter: " + str(sysCounter))

maxGuess = input("Guess the number between 1 and: ")
randNum = random.randint(1, int(maxGuess))
systemGuess(int(maxGuess), randNum)
