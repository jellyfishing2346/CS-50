# Create a grocery array and list dictionary
groceryArray = []
list = {}

# Design a while loop to loop through the grocery dictionary
while True:
    try:
        # Retrieve the user's input
        itemCollect = input("Item: ")
        itemCollect = itemCollect.upper()
        # Going through the grocery array
        groceryArray.append(itemCollect)
        groceryArray.sort()
    except EOFError:
        for itemCollect in groceryArray:
            if itemCollect in list:
                list[itemCollect] += 1
            else:
                list[itemCollect] = 1
            for index in list:
                print(str(list[index]) + " " + index)
            break
        else:
            continue
