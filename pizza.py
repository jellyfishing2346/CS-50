import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

tableInfo = []
if sys.argv[1].endswith(".csv"):
    try:
        with open(sys.argv[1], "r") as csvFileInfo:
            read = csv.DictReader(csvFileInfo)
            for index in read:
                tableInfo.append(index)
    except FileNotFoundError:
        sys.exit("File does not exist")
else:
    sys.exit("Not a CSV file")

print(tabulate(tableInfo, index="key", tablefmt="grid"))