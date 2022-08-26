import re

# Main function
def main():
    print(count(input("Text: ")))

# Count function
def count(s):
    um = re.findall(r"\b\W*um\W*", s, re.IGNORECASE)
    if not um:
        return len(um)


if __name__ == "__main__":
    main()