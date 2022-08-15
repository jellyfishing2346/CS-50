# Create a dictionary called grocery
grocery = {}

# Design a forever loop
while True:
     try:
        item = input("")
     except EOFError:
         # Check if the item is already in the dictionary, add 1 to the count
         for (count, index) in sorted(grocery.items()):
               print(index, count)
         break
     item = item.strip().upper()
     try:
         grocery[item]
     except KeyError:
         grocery[item] = 1
     else:
         grocery[item] += 1




