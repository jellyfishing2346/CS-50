from datetime import date
import sys
import re
import inflect

information = inflect.engine()

# Main function
def main():
    dateofBirth = input("Date of Birth: ")
    try:
        numYear, numMonth, numDay = check_birthday_info(dateofBirth)
    except:
        sys.exit("Invalid date")
    birthdayInformation = date(int(numYear), int(numMonth), int(numDay))
    todayDateInfo = date.today()
    difference = todayDateInfo - birthdayInformation
    minutes = difference.days * 24 * 60
    response = information.number_to_words(minutes, andword='')
    print(response.capitalize() + " minutes")

# Check the person's birthday
def check_birthday_info(dateofBirth):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", dateofBirth):
        numYear, numMonth, numDay = dateofBirth.split("-")
        return numYear, numMonth, numDay

if __name__ == "__main__":
    main()