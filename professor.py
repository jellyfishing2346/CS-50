import random

# Create a main function to determine to get the user's score
def main():
levelInfo = retrieveLevel()
scoreResult = game(levelInfo)
print("Score: ", scoreResult)

# This function is to know what level the user is on
def retrieveLevel():
    while True:
        try:
            levelInfo = int(input("Level: "))
            if levelInfo in [1,2,3]:
                 break
        except:
            pass
    return levelInfo

# Random integers for each level for the game
def randomIntegers(levelInfo):
    if levelInfo == 1:
        index = random.radint(0,9)
        count = random.radint(0,9)
    elif levelInfo == 2:
        index = random.radint(10,99)
        count = random.radint(10,99)
    elif levelInfo = 3:
        index = random.radint(100,999)
        count = random.radint(100,999)
    return index, count

# This found generates the number of rounds
def roundGenerator(index, count):
    attempts = 1
    while attempts <= 3:
        try:
            equation = int(input(f"{index} + {count} = "))
            if equation == (index + count):
                return True
            else:
                print("EEE")
                attempts += 1
        except:
            print("EEE")
            attempts += 1
            pass
        print(f"{index} + {count} = {index + count}")
        return False

 # This function will start the game
 def game(levelInfo):
    round = 0
    scoreTrack = 0
    while round < 10:
        index, count = randomIntegers(levelInfo)
        responseAnalyze = roundGenerator(index, count)
        if responseAnalyze == True:
            scoreTrack += 1
        round += 1
    return scoreTrack

# Main function set up
if __name__ == "__main__:
    main()