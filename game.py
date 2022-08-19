import random

# Retrieve level info
while True:
    try:
        levelInfo = int(input("Level: "))
        if levelInfo > 0:
            break
    except:
            pass

# Generate random numbers
randomNumber = random.randint(1, levelInfo)

# Guess a number and check
while True:
    try:
        userGuess = int(input("Guess: "))
        if userGuess > 0:
            if userGuess < randomNumber:
                print("This number is too small")
            elif userGuess > randomNumber:
                print("This number is too large")
            else:
                print("This number is correct")
                break
    except:
        pass