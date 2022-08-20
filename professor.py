import random

# Create a main function to determine to get the user's score
def main():
    levelInfo = retrieveLevel()
    correct = randomIntegers(levelInfo)
    print("Score: ", correct)

# This function is to know what level the user is on
def retrieveLevel():
    while True:
        try:
            index = int(input("Level: "))
            if not index in range(1,4):
                raise ValueError
            else:
                return input
        except ValueError:
            continue

# Random integers for each level for the game
def randomIntegers(levelInfo):
    scoreTrack = 0
    if levelInfo == 1:
        for _ in range(10):
            first = random.randint(10,99)
            second = random.randint(10,99)
            rounds = 0
            while True:
                if rounds == 3:
                    print(f'{first} + {second} = {first + second}')
                    break
                input = int(input(f'{first} + {second} = '))
                if index == first + second:
                    scoreTrack += 1
                    break
                else:
                    print('EEE')
                    rounds += 1
                return scoreTrack
        elif levelInfo == 2:
            for _ in range(10):
                first = random.randint(10,99)
                second = random.randint(10,99)
                rounds = 0
                while True:
                    if rounds == 3:
                        print(f'{first} + {second} = {first + second}')
                        break
                    index = int(input(f'{first} + {second} = '))
                    if index == first + second:
                        scoreTrack += 1
                        break
                    else:
                        print('EEE')
                        rounds += 1
                return scoreTrack
            elif levelInfo == 3:
            for _ in range(10):
                first = random.randint(100,999)
                second = random.randint(109,999)
                rounds = 0
                while True:
                    if rounds == 3:
                        print(f'{first} + {second} = {first + second}')
                        break
                    index = int(input(f'{first} + {second} = '))
                    if index == first + second:
                        scoreTrack += 1
                        break
                    else:
                        print('EEE')
                        rounds += 1
                return scoreTrack

# Main function set up
if __name__ == '__main__':
    main()