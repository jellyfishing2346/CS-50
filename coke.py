# Track the variable for the amount of change that the user owes
due = 50

#
while due >  0:
    print("Amount due: ", due)
    coins = int(input("Insert coin: "))
    if coin in [25, 10, 5]:
        due -= coins

# Calculate the change owed
change = abs(due)

# Display the result
print("Change owed: ", change)
