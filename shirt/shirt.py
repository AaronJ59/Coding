
import sys
import os
from PIL import Image, ImageOps

def main():
    check_length(sys.argv)
    check_extension(sys.argv)
    putshirtonimage(sys.argv)



def check_length(arg):
    if len(arg) < 2:
        sys.exit("Too few command-line arguments")
    if len(arg) > 3:
        sys.exit("Too many command-line arguments")

def check_extension(arg):
    if not arg[1].endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Wrong format")
    if not arg[2].endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Wrong format")
    root1, ext1 = os.path.splitext(arg[1])
    root2, ext2 = os.path.splitext(arg[2])
    if ext1 != ext2:
        sys.exit("Both files should have the same extension")

def putshirtonimage(arg):
    shirt = Image.open("shirt.png")
    image = Image.open(arg[1])
    width, height = shirt.size
    fittedimage = ImageOps.fit(image, (width, height))
    fittedimage.paste(shirt, shirt)
    fittedimage.save(arg[2])


if __name__ == "__main__":
    main()
