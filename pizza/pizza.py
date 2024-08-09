import sys
from tabulate import tabulate
import csv


def main():
    checklength(sys.argv)
    filetotable(sys.argv[1])


def checklength(argv):
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(argv) > 2:
        sys.exit("Too many command-line arguments")
    if not argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


def filetotable(csvfile):
    try:
        with open(csvfile, "r") as file:
            if csvfile == "sicilian.csv":
                reader = csv.DictReader(file)
                table = []
                headers = ["Sicilian Pizza", "Small", "Large"]
                for row in reader:
                    table.append([row["Sicilian Pizza"], row["Small"], row["Large"]])
                print(tabulate(table, headers, tablefmt="grid"))
            if csvfile == "regular.csv":
                reader = csv.DictReader(file)
                table = []
                headers = ["Regular Pizza", "Small", "Large"]
                for row in reader:
                    table.append([row["Regular Pizza"], row["Small"], row["Large"]])
                print(tabulate(table, headers, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
