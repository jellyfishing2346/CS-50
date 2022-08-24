import sys
import csv

# Main function
def main():
    check_command_line()
    response = []
    # Open the file
    try:
        with open(sys.argv[1]) as csvFile:
            readInfo = csv.DictReader(csvFile)
            for index in readInfo:
                name = index['name'].split(",")
                # Add the name to the dictionary
                response.append({"first": name[1].lstrip(), "last": name[0], "house": index['house']})
    # If the file is not opening, then it doesn't exist
    except FileNotFoundError:
        sys.exit("Could not read {sys.argv[1]}")

    # Write the csv file with the following information
    with open(sys.argv[2], "w") as csvFile:
        write = csv.DictReader(csvFile, fieldnames=["first", "last", "house"])
        write.writerow({"first": "first", "last": "last", "house": "house"})
        for index in response:
            write.writerow({"first": index['first'], "last": index['last'], "house": index['house']})

# This function checks the command line argument
def check_command_line():
    # Determine how elements exist in the command line argument
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # Determine if the file is a CSV file
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")

if __name__ = "__main__":
    main()