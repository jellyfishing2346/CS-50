from csv import reader, DictReader
from sys import argv, exit


def main():
    # Check for the command-line usage
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)
   # Create a bunch of variables
    DNA_bases = argv[1]
    sequences = argv[2]
    # Open the CSV file and convert to dictionary
    with open(DNA_bases, "r") as csvFile:
        reader = DictReader(csvFile)
        dictList = list(reader)

    # Open the sequence file to be converted to a list
    with open(sequences, "r") as file:
        sequences = file.read()
    # Count the number of STR's
    maximum = []
    for index in range(1, len(reader.fieldnames)):
        samples = reader.fieldnames[index]
        maximum.append(0)
    # Loop through each sequence individually for STR
    for count in range(len(sequences)):
        counting = 0
    # If a match is found, repeat count for STR
    if sequences[count:(count + len(samples))] == samples:
        total = 0
        while sequence[(count + total):(count + total + len(samples))] == samples:
            counting += 1
            total += len(samples)
    # Update max count, if there is a new maximum number of repeats
    if counting > maximum[index - 1]:
        maximum[index - 1] = samples
    # Compare the data to determine the suspect's name
    for index in range(len(dictList)):
        match = 0
        for count in range(1, len(reader.fieldnames)):
            if int(maximum[count - 1]) == int(dictList[index][reader.fieldnames[count]]):
                match += 1
            elif match == (len(reader.fieldnames) - 1):
                print(dictList[index]['name'])
                exit(0)
            else:
            print("No match")
    return


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
