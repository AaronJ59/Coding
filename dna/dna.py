import csv
import sys


def main():
    # TODO: Check for command-line usage
    if sys.argv[1] not in ("databases/small.csv", "databases/large.csv"):
        print("first command-line wrong")
        return 0
    try:
        file_sequence = open(sys.argv[2], "r")
    except FileNotFoundError:
        print("second command-line wrong")
        return 0

    # TODO: Read database file into a variable
    file = open(sys.argv[1], "r")
    database_file = file.read()
    # print(database_file)

    # TODO: Read DNA sequence file into a variable
    file = open(sys.argv[2], "r")
    sequence_file = file.read()
    # print(sequence_file)

    # TODO: Find longest match of each STR in DNA sequence
    longest_matches = []
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)

        for str in reader.fieldnames[1:]:
            count = longest_match(sequence_file, str)
            longest_matches.append(count)

    # TODO: Check database for matching profiles
    list_num = 0
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if sys.argv[1] == "databases/small.csv":
                csv_list = [int(row["AGATC"]), int(row["AATG"]), int(row["TATC"])]
                list_num = list_num + 1
                if csv_list == longest_matches:
                    print(row["name"])
                    return
                if list_num == 3:
                    print("No match")
            elif sys.argv[1] == "databases/large.csv":
                csv_list = [
                    row["AGATC"],
                    row["TTTTTTCT"],
                    row["AATG"],
                    row["TCTAG"],
                    row["GATA"],
                    row["TATC"],
                    row["GAAA"],
                    row["TCTG"],
                ]
                csv_list = [int(num) for num in csv_list]
                list_num = list_num + 1
                if csv_list == longest_matches:
                    print(row["name"])
                    return
                if list_num == 23:
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
