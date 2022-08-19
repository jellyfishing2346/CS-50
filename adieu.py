# Import the package called inflect
import inflect

# Store all types of words such as plurals, nouns, ordinals, convert numbers to words
word = inflect.engine()

# Store the names
nameStorage = ()
while True:
    try:
        userName = input("Name: ")
    except EOFError:
        adieuName = word.join(nameStorage)
        print(f"Adieu, adieu to {adieu}")
        break
    nameStorage = nameStorage + (userName)