import sys

# Main function
def main():
    check_command_line()
    # Open the file
    try:
        with open(sys.argv[1], "r") as fileInfo:
            lineInfo = fileInfo.readlines()
        lineInfo.close()
            # If the file is not opening
    except FileNotFoundError:
         sys.exit("File does not exist")
    # Loop through the lines to see if # or whitespace is present
    count = 0
    for index in lineInfo:
        if check_command_line_is_empty(index) == True:
            count += 1
    print(count)

# Check the command line argument
def check_command_line():
    # Check the elements in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Determine if the file is python
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

# Check the command line is empty
def check_command_line_is_empty(index):
    if index.lstrip().startswith('#'):
        return False
    elif index.isspace():
        return False
    return True