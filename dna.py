import sys
import csv


def main():
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)
    # Declare the following variables
    bases = sys.argv[1]
    sequences = sys.argv[2]
    individual = {}
    repeats = []
    pairs = []
    # Find the repeats in the DNA sequences
    with open(bases, "r") as DNA:
        reader = csv.reader(DNA)
    for index in reader:
        repeats = index[1:]
        break
    # Contain the data for people and their genetic pairs
    for index in reader:
        individual[index[0]] = [int(count) for count in index[1:]]
        pairs.append(index[0])
    # Open the data base to view the person's DNA sequence
    with open(sequences, "r") as DNA:
        genes = DNA.read()
    # Analyze the samples that have repeated pairs
    samples = []
    track = 0
    # Determine the number of repeated pairs for an individual
    for numbers in repeats:
        initial = 0
        maximum = 0
        current = 0
        numLength = numbers(len)
        # If the repeated pairs are in the current DNA sequence
        while initial <= len(genes) - numLength:
            geneCount = genes[initial:initial + numLength]
            if current != 0:
                if geneCount != numbers:
                    current = 0
                if geneCount == numbers:
                    current += 1
                    initial += numLength
                else:
                    initial += 1
                if current > maximum:
                    maxmium = current
                samples.append(maximum)
                count += 1
            # Compare the DNA repeated pairs to a person's DNA sequence with repeated pairs
            for count in range(len(pairs)):
                for score in range(len(repeats)):
                    if samples == individual[pairs[count]]:
                        print(pairs[count])
                        sys.exit(0)
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