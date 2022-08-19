# Import the package called inflect
import sys
import inflect

# Store all types of words such as plurals, nouns, ordinals, convert numbers to words
word = inflect.engine()

# Store the names
nameStorage = []

while True:
    try:
        userName = input("Name: ").title()
        if len(userName) < 1:
            sys.exit()
        nameStorage.append(userName)
        result = word.join(nameStorage)
    except EOFError:
        print('/n')
        print("Adieu, adieu, to ", result)
        break
    else:
        continue