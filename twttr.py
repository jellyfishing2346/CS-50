# Prompt the user to enter some input
text = input("Input: ")

# Account for all cases of the vowels
for ch in "aAeEiIoOuU":
    text = text.replace(ch, '')

# Display the final text
print("Output: ", text)
