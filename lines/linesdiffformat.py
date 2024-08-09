import sys

def main():
    check_arg(sys.argv)
    returnedvalue = read_file(sys.argv[1])
    print("Total Lines:", returnedvalue)



def check_arg(argv):
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not argv[1].endswith(".py"):
        sys.exit("Not a python file")



def read_file(myfile):
    try:
        with open(myfile) as file:
            listoflines = file.readlines()
            removelinecount = 0
            for line in listoflines:
                if line.isspace():
                    removelinecount += 1
                if line.lstrip().startswith("#"):
                    removelinecount += 1
            truelinecount = len(listoflines) - removelinecount
            return truelinecount





    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__=="__main__":
    main()
