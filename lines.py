import sys

# Main function
def main():
     # Check the elements in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    lineInfo = 0
    # Determine if the file is python
    if ".py" not in sys.argv[1]:
        try:
            fileInfo = open(sys.argv[1], "r")
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")

    for index in fileInfo:
        if index.lstrip().startswith('#'):
            pass
        elif index.isspace():
            pass
        else:
            lineInfo += 1

    print(lineInfo)
    fileInfo.close()