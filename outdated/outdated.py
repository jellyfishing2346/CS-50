# Create a month array
numMonth = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# Design a forever loop to go through the date's proper format with month array
while True:
    date = input("Date: ").strip()
    if "/" in date:
        date = date.split("/")
        try:
            day = int(date[1])
            month = int(date[0])
        except ValueError:
            # Conversion of string letters to integer numbers in progress
            continue
        else:
            day = int(date[1])
            year = date[2]
        if day > 31:
            continue
        elif month > 12:
            continue
        year = date[2]
        month = date[0]
        day = date[1]
        print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")
        break
    elif "," in date:
        date = date.split(",")
        year = date[1]
        (month, day) = date[0].split(" ")
        try:
            month = numMonth.index(month) + 1
            day = int(day)
        except IndexError:
            continue
        except ValueError:
            continue
        else:
            if day > 31:
                continue
            print(f"{year}-{month:02}-{day:02}")
            break