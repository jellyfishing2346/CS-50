# Input validation: The height has to be greater than 0 and less than 9
from cs50 import get_int
while True:
    try:
       height = int(input("Height: "))
       if height >= 1 and height <= 8:
        break
       else:
        print("", end="")
# The number of spaces accounted
spaces = 1
# Account index for rows and count for columns
for count in range(height):
    for spaces in range(height - count - 1):
        print("", end="")
    for index in range(count + 1):
        print("#", end="")
    print()





