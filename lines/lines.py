import sys


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file")


try:
    with open(sys.argv[1]) as file:
        listoflines = file.readlines()
        removelinecount = 0
        for line in listoflines:
            if line.isspace():
                removelinecount += 1
            if line.lstrip().startswith("#"):
                removelinecount += 1
        truelinecount = len(listoflines) - removelinecount
        print("Total lines:", truelinecount)





except FileNotFoundError:
    sys.exit("File does not exist")



