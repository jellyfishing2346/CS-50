# Create a dictionary called groceries
  groceryDict = {}

# Use a foreverloop to go through that dictionary
  while True:
      try:
          groceryDict = input("")
      except EOFError:
          # Determine if the dictionary is empty
          for (index, itemCollect) in sorted(groceries.items()):
              print(index, itemCollect)
          break
      groceryDict = groceryDict.strip().upper()
      try:
          [grocery]
      except KeyError:
          groceries[grocery] = 1
      else:
          groceries[grocery] += 1
