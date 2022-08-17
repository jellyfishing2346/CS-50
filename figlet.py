import sys
from random import choice
from pyfiglet import Figlet

randomTexts = Figlet()
fontUsuage = randomTexts.getFonts()

if len(sys.argv) == 1:
    user = input("Input: ")
    fontChoice = choice(fontUsuage)
    randomTexts.setFont(font=user)
    print(figlet.renderText(fontChoice))
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fontChoice:
        user = input("Input: ")
        fontChoice = sys.argv[2]
        figlet.setFont(font=user)
        print(figlet.renderText(fontChoice))
    else:
        sys.exit("Invalid usuage")
else:
    sys.exit("Invalid usuage")