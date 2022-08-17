import sys
from random import choice
from pyfiglet import Figlet


num_args = len(sys.argv)

if num_args == 1:
    font = choice(Figlet().getFonts())
elif num_args == 3 and sys.argv[1] in ["-f", "--font"]:
    font = sys.argv[2]
else:
    print('Invalid usage')
    sys.exit(1)

Figlet.setFont(font=font)
print(Figlet.renderText(input('Input: ')))