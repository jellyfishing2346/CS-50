# Prompt the user to enter a greeting
response = input("Greeting: " )

# New response to encounter user modifications
new_response = response.strip().lower()

# If the user enters Hello, print $0
if new_response == "Hello":
    print("$0")

# If the user enters Hello, Newman prints $0
elif new_response == "Hello, Newman":
    print("$0")

# If the user enter How you doing?, prints $20
elif new_response == "How you doing?":
    print("$20")

# If the user enter What's happening?, print $100
elif new_response == "What's happening?":
    print("$100")

# If the user enters other case by default print $100
else:
    print("$100")