# Prompt the user to change
from cs50 import get_int
while True:
    cents = get_int("Change owed: ")
    if (cents > 0):
        break
cents = round(cents * 100)
track = 0
# The number of quarters
while cents >= 25:
    cents = cents - 25
    track += 1
# The number of dimes
while cents >= 10:
    cents = cents - 10
    track += 1
# The number of nickels
while cents >= 5:
    cents = cents - 5
    track += 1
# The number of pennies
while cents >= 1:
    cents = cents - 1
    track += 1
# Print the total number of coins
print("The total amount of coins: ", track)