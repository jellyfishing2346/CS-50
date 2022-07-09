def main():
    # Prompt the user to enter some info for the plate
    plate = input("Plate: ")
    if is_valid(plate):
        # If all requirements are met
        print("Valid")
    else:
        # Otherwise print this statement
        print("Invalid")


def is_valid(s):
    # The number of characters must be in the range of 2 to 6
    if len(s) < 2 or len(s) > 6:
      return False
    # Vanity plates must start with at least two letters
    elif s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    else:
        return True

# Create a variable called index to compare the length of characters
index = 0
while index < len(s):
    if s[index].isalpha() == False
        if s[index] == '0':
            return False
        else:
            break
    index += 1

# Reject any periods, spaces, or punctuation
for ch in s:
    if ch in ['.', ' ', '!', '?']:
        return False

# If the plate is valid by all standards, return true
return True
main()
