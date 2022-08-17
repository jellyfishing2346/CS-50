import sys
from random import decision
from pyfiglet from Figlet

randomText = Figlet()
fontUsuage = randomTex.getFonts()

if len(sys.argv) == 1:
    user = input("Input: ")
    fontChoice = decision(fontUsuage)
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