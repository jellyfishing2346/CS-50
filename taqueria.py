# Create a menu for Felipe's taqueria
menu = {
    "Bajo Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

# Set the total price
price = 0

# Created a while loop to determine what food the person ordered and to list their price
while True:
    try:
        item = input("Item: ")
        item = item.title()

        for order in menu:
            if item == order:
                price += menu[order]
                print("Total: $" + str(price) + "0")
            else:
                continue
    except EOFError:
            print("\n")
            break
     else:
            continue
