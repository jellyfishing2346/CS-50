import random

def main():

    level = get_level()

    correct = generate_integer(level)

    print("Score:", correct)



def get_level():

    while True:

        try:

            index = int(input("Level: "))

            if index not in range(1,4):

                raise ValueError

            else:

                return index

        except ValueError:

            continue



def generate_integer(level):

    scoreTracking = 0

    if level == 1:

        for _ in range(10):

            first = random.randint(0,9)

            second = random.randint(0,9)

            rounds = 0

            while True:

                if rounds == 3:

                    print((f"{first} + {second} = {first+second}"))

                    break

                index = int(input(f"{first} + {second} = "))

                if index == first + second:

                    scoreTracking += 1

                    break

                else:

                    print('EEE')

                    rounds += 1

        return scoreTracking

    elif level == 2:

        for _ in range(10):

            first = random.randint(10,99)

            second = random.randint(10,99)

            rounds = 0

            while True:

                if rounds == 3:

                    print((f'{first} + {second} = {first+second}'))

                    break

                index = int(input(f'{first} + {second} = '))

                if index == first + second:

                    scoreTracking += 1

                    break

                else:

                    print('EEE')

                    rounds += 1

        return scoreTracking

    elif level == 3:

        for _ in range(10):

            first = random.randint(100, 999)

            second = random.randint(100, 999)

            rounds = 0

            while True:

                if rounds == 3:

                    print((f'{first} + {second} = {first+second}'))

                    break

                index = int(input(f'{first} + {second} = '))

                if index == first + second:

                    scoreTracking += 1

                    break

                else:

                    print('EEE')

                    rounds += 1

    return scoreTracking



if __name__ == "__main__":

    main()