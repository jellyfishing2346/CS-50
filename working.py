import re
import sys

# Main function
def main():
    print(convert(input("Hours: ")))

# Convert function
def convert(s):
    try:
        correct = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
        if correct:
            time = correct.groups()
            if int(time[1]) > 12 or int(time[5]) > 12:
                raise ValueError
            # The first time in 24 hours
            first = time_format(time[1], time[2], time[3])
            # The second time in 24 hours
            second = time_format(time[5], time[6], time[7])
            return first + " to " + second
        else:
            raise ValueError
    except ValueError:
        sys.exit("ValueError")

# Time format function
def time_format(hours, minutes, AM_PM):
    if AM_PM == 'PM':
        if int(hours) == 12:
            numHours = 12
        else:
            numHours = int(hours) + 12
    else:
        if int(hours) == 12:
            numHours = 0
        else:
            numHours = int(hours)
    if minutes == None:
        numTime = f"{numHours:02}" + ":00"
    else:
        numTime = f"{numHours:02}" + ":" + minutes
    return numTime

if __name__ == "__main__":
    main()