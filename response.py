from validator_collection import validators

# Main function
def main():
    emailInfo = input("What's your email address? ")
    try:
        valid = validators.email(emailInfo)
        print("Valid")
    except:
        print("Invalid")

if __name__ == "__main__":
    main()