import csv
import sys


def main():
    # Check for the command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")
   # Create a bunch of variables
    verification = True
    STRList = []
    person = []
    # Copy each potential suspect to the database
    with open(sys.argv[1], "r") as STR:
        analyzeSTR = csv.reader(STR)
        for index in analyzeSTR:
            if verification:
                STRList.append(index)
                verification = False
            else:
                person.append(index)
                Samples = STRList[0]
                Samples.remove("name")
                print(person)
                print(Samples)
                # Duplicate the DNA sequence
                with open(sys.argv[2], "r") as txt:
                    readtxt = csv.reader(txt)
                    for count in readtxt:
                        sequences = count
                        txt = sequences[0]
                        print(txt)
                        # Dictionary for STR count
                        dictionary = {}
                        for character in range(len(person)):
                            for STR in Samples:
                                total = 0
                                maximum = 0
                                while total < len(txt):
                                    repeats = 0
                                    while STR == txt[total:total+len(STR)]:
                                        repeats += 1
                                        total += len(STR)
                                    if repeats > maximum:
                                        maximum = repeats
                                        total += 1
                                        dictionary[STR] = maximum
                                        print(STR, maximum)
                                        for individual in range(len(txt)):
                                            if str(dictionary[STR]) == str(person[individual][STR + 1]):
                                                verification = True
                                            else:
                                                verification = False
                                                break
                                            if verification:
                                                print(person[individual][0])
                                                break
                                            if not verification:
                                                print("No Match")





    #
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
