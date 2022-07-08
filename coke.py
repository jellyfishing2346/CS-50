# Track the variable for the amount of change that the user owes
due = 50

# Loop until the amount owed is greater than 0
while due >  0:

# Display the amount due
    print("Amount due: ", due)

# Input the amount the user has in terms of coins
    coins = int(input("Insert coin: "))

# If the cents is 25, 10, or 5 subtract the owed amount by coins
    if coins in [25, 10, 5]:
        due -= coins

# Calculate the change owed
change = abs(due)

# Display the result
print("Change owed: ", change)
