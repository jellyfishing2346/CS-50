import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

# Evaluating the given random text
if len(sys.argv) == 1:
    isFont = True
elif len(sys.argv) == 3:
    isFont = False
elif not sys.argv[1] == "-f" or sys.argv[1] == "--font":
    isFont = False
else:
    print("Invalid usuage")
    sys.exit(1)

# This will list the fonts that are avaiable from the figlet package
figlet.getFonts()

if isFont == False:
    try:
        fontUser = figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usuage")
        sys.exit(1)
else:
    fontUser = random.choice(figlet.getFonts())
    figlet.setFont(font=fontUser)

# Get the user to input some random text
text = input("Input: ")

# Output text in the font with a code using s as a str
response = figlet.renderText(text)

# Display the output text
print("Output: ")
print(response)
sys.exit(0)
