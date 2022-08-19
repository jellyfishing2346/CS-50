# Import the package called inflect
import inflect

# Store all types of words such as plurals, nouns, ordinals, convert numbers to words
word = inflect.engine()

# Store the names
nameStorage = []

while True:
    try:
        # Retrieve the user's input
        userName = input("Name: ")
        nameStore.append(userName)
    except EOFError:
        # Create a new line and then terminate the loop
        print()
        break
# Print through the use of the inflect module
result = words.join(nameStorage)
print("Adieu, adieu, to " + result)