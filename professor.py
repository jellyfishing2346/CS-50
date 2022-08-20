import random
import sys

# Create a main function to determine to get the user's score
def main():
    levelInfo = retrieveLevel()

    mistakes = 1
    scoreTrack = 0

    for track in range(10):
        index = randomIntegers(levelInfo)
        for check in range(1):
            count = randomIntegers(levelInfo)

            result = index + count
            equation = input(f"{index} + {count} = ")

            if int(equation) == result:
                scoreTrack += 1

            while int(equation) != result:
                mistakes += 1
                print("EEE")
                equation = input(f"{index} + {count} = ")
                if mistakes >= 3:
                    print(result)
                    sys.exit("Score: " + str(scoreTrack))

    print("Score: " + str(scoreTrack))

# This function is to know what level the user is on
def retrieveLevel():
    levelInfo = input("Level: ")

    if levelInfo.isalpha() or int(levelInfo) <= 0 or int(levelInfo) > 3:
        input("Level: ")
    else:
        levelInfo = int(levelInfo)
        for game in [1,2,3]:
            if levelInfo == game:
                return levelInfo

# Random integers for each level for the game
def randomIntegers(levelInfo):
    try:
        if levelInfo == 1:
            return random.randint(0,9)
        elif levelInfo == 2:
            return random.randint(10,99)
        elif levelInfo == 3:
            return random.randint(100,999)
    except:
        raise ValueError

# Main function set up
if __name__ == '__main__':
    main()