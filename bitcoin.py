import requests
import sys
import bitcoin

# Test the bitcoin to see if its valid
if len(sys.argv) == 2:
    try:
        bitcoin = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

# The value of the exising bitcoin, then exit out from it
try:
    value = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    view = value.json()
    bitcoinToDollars = value["bpi"]["USD"]["rate"]
    bitcoinToDollars = bitcoinToDollars.replace(",","")
    dollars = float(bitcoinToDollars) * float(sys.argv[1])
    print(f"${dollars:,4f}")

except requests.RequestException:
    print("RequestException")
    sys.exit(1)