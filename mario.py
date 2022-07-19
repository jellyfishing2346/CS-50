# Input validation: The height has to be greater than 0 and less than 9
from cs50 import get_int
while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break
# Account index for rows and count for columns
for index in (0, height, 1):
    for count in (0, height, 1):
        if (index + count < height - 1):
            print(" ", end="")
        else:
            print("#", end="")
        print()
