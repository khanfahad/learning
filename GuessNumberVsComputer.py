import random

# function that takes minimum and maximum value and returns the integer in the middle
def returnHalf(minNum, maxNum):
    rangeNum = int((maxNum - minNum)/2)
    return int(rangeNum + minNum)

# function that takes in the range from 1 and maxGuess and the randomly-generated number
def systemGuess(maxGuess, randNum):
    minNum = 0
    sysCounter = 0 # tracks the number of tries by computer
    sysGuess = 0
    maxNum = maxGuess
    while (sysGuess != randNum):
        sysGuess = int(returnHalf(minNum,maxNum))
        sysCounter += 1
        if (int(sysGuess) < randNum):
            minNum = sysGuess # minimum becomes the system guess and maximum remains the maximum
        elif (int(sysGuess) > randNum):
            maxNum = sysGuess # maximum becomes the syster guess and minimum remains the same
        else:
            break
    return sysCounter

maxGuess = input("Guess the number between 1 and: ") # get user input to set the range between 1 and n
randNum = random.randint(1, int(maxGuess)) #generate random number between the range
sysCounter = systemGuess(int(maxGuess), randNum)

userCounter = 0 # tracks number of guesses by user
userGuess = 0
while (userGuess != randNum): # runs the loop until guessed
    userGuess = input("What is your guess: ")
    userCounter += 1
    if (int(userGuess) < randNum):
        print("You're too LOW, try again...")
    elif (int(userGuess) > randNum):
        print("You're too HIGH, try again...")
    else:
        print("YOU GOT IT!")
        break # breaks the loop when correct guess is made
print("You guessed it in " + str(userCounter) + " tries.")
print("It took the system " + str(sysCounter) + " tries.")
if userCounter < sysCounter:
    print("CONGRATULATIONS, you beat the system!")
else:
    print("The system owned you!")
