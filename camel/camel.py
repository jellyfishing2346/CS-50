# Prompt the user to enter a name
camel_case =  input("camelCase: ")

# Display the snake case
print("snake_case: ", end = "")

# Loop through the letters
for blank in camel_case:

# If encounter uppercase letters with no space, evaluate with conditionals
    if blank.isupper():
        print("_" + blank.lower(), end = "")
    else:
        print(blank, end = "")

# Display the final result
print()