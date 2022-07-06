# Prompt the user to enter a greeting
response = input("Greeting: " ).lower(check50 cs50/problems/2022/python/bank)

# If the user enters Hello, print $0
if response == "Hello":
    print("$0")

# If the user enters Hello, Newman prints $0
elif response == "Hello, Newman":
    print("$0")

# If the user enter How you doing?, prints $20
elif response == "How you doing?":
    print("$20")

# If the user enter What's happening?, print $100
elif response == "What's happening?":
    print("$100")

# If the user enters other case by default print $100
else:
    print("$100")