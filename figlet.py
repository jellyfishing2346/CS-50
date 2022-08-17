import sys
from random import choice
from pyfiglet import Figlet

randomText = Figlet()
fontUsuage = randomTexts.getFonts()

if len(sys.argv) == 1:
    user = input("Input: ")
    fontChoice = choice(fontUsuage)
    randomText.setFont(font=user)
    print(figlet.renderTexts(fontChoice))
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fontChoice:
        user = input("Input: ")
        fontChoice = sys.argv[2]
        figlet.setFont(font=user)
        print(figlet.renderTexts(fontChoice))
    else:
        sys.exit("Invalid usuage")
else:
    sys.exit("Invalid usuage")