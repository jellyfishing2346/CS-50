import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

# Evaluating the given random text
if len(sys.argv) == 1:
    isFont = True
elif len(sys.argv) == 3:
    isFont = False
else:
    print("Invalid usuage")
    sys.exit(0)

# This will list the fonts that are avaiable from the figlet package
figlet.getFonts()

if isFont == False:
    try:
        fontUser = figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usuage")
        sys.exit(0)
else:
    fontUser = random.choice(figlet.getFonts())

# Get the user to input some random text
text = input("Input: ")

# Output text in the font with a code using s as a str
response = figlet.renderText(text)

# Display the output text
print("Output: ")
print(response)