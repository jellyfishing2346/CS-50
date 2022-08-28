import re

# Main function
def main():
    print(count(input("Text: ")))

# Count function
def count(s):
    um = re.findall(r"\b\W*um\W*", s, re.IGNORECASE)
    return len(um)

# Um conditional
def um_conditional(um):
    if um == "um" or um == "UM" or um == "Um":
        return len(um)

if __name__ == "__main__":
    main()
