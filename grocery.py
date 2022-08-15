# Create a dictionary called grocery
grocery = {}

# Design a forever loop
while True:
     try:
        item = input().upper()
     except KeyboardInterrupt:
            print("Interruption/n")
     # Check if the item is already in the dictionary, add 1 to the count
     if item not in grocery:
            grocery[item] = 1
      # Otherwise take the item to be added as a new entry to the dictionary
     else:
        grocery[item] += 1
     try:
      # Create a list variable
      groceryList = sorted(dict.items(grocery))
     except EOFError:
         for count, index in groceryList:
            print(index, count, item)