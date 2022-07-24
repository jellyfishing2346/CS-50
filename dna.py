import csv
import sys


def main():
    # Check for command line usage
    n = len(sys.argv)
    if n != 3:
        print("python dna.py data.csv sequence.txt")
        exit(0)


# Read database file into a variable
with open(sys.argv[1], 'r') as csvfile:
    dataInfo = csv.reader(csvfile)
    data = [row for row in dataInfo]

# Read DNA sequence file into a variable
with open(sys.argv[2], 'r') as sequences:
    DNA = sequences.read()
repeats = []
# Find the longest match of each STR in the DNA sequence
for index in range(1, len(data[0])):
    counting = 1
    string = data[0][index]
    while string * counting in DNA:
        counting += 1
    repeats.append(str(counting - 1))
# Check database for matching profiles
for calculate in range(1, len(data)):
    if data[calculate][1:len(data[0])] == repeats:
        print(data[calculate][0])
        exit(0)
print('No Match')


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length
            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()

