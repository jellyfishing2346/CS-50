# Create a grocery dictionary
grocery = {}

# Design a while loop to loop through the grocery dictionary
while True:
    try:
        # Retrieve the user's input
        item = input()
        # Determine if the item is already in the grocery dictionary
        if item.lower() in grocery:
            grocery[item.lower()] += 1
        else:
            grocery[item.lower()] = 1
    except EOFError:
        # Print all grocery items in alphabetic order
        for list in sorted(grocery.list):
            print(grocery[list], list.upper())
        # Terminate the while loop
        break