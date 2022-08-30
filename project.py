import sys
import csv

# Main function
def main():
    check_correct_argument_info()
    information = []
    try:
        with open(sys.argv[1]) as csvFileInfo:
            read = csv.DictReader(csvFileInfo)
            for index in read:
                information.append(index)
    except FileNotFoundError:
        sys.exit("Couldn't read the CSV file")
    response = []
    for index in information:
        character = select_character(index[" trait"])
        dateOfBirth = select_age(index[" birthYear"])
        response.append({"name": index["name"], "character": character, "dateOfBirth": dateOfBirth})
    with open(sys.argv[2], "w") as fileInformation:
        writing = csv.DictWriter(fileInformation, fieldnames=["name", "character", "dateOfBirth"])
        writing.writeheader()
        writing.writerows(response)
#        writing.writerow("name" == "name", "character" == "character", "dateOfBirth" == "dateOfBirth")
#        for index in response:
#            writing.writerow("name" == index["name"], "character" == index["character"], "dateOfBirth" == index["dateOfBirth"])

# Check the command argument line
def check_correct_argument_info():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("No CSV files")

# Character traits function
def select_character(charInput):
    charInput = charInput.strip()
    if charInput in ["funny", "quirky", "buffon"]:
        return "Class Clown"
    elif charInput in ["gullible", "emo", "dull"]:
        return "UnInterested"
    elif charInput in ["angry", "annoying", "arrognant"]:
        return "Unlikeable"
    elif charInput in ["mischievous"]:
        return "Untolerable"
    else:
        return "Character type unknown"

# Determine how old the character is based on there year
def select_age(yearInfo):
    characterAge = 2022 - int(yearInfo)
    dateOfBirth = characterAge
    return "Age " + str(dateOfBirth)

if __name__ == "__main__":
    main()
