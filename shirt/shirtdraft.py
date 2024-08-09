import sys
import os
from PIL import Image, ImageOps


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Wrong format")
if not sys.argv[2].endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Wrong format")

root1, ext1 = os.path.splitext(sys.argv[1])
root2, ext2 = os.path.splitext(sys.argv[2])

if ext1 != ext2:
    sys.exit("Both files should have the same extension")


shirt = Image.open("shirt.png")
image = Image.open(sys.argv[1])
width, height = shirt.size
fittedimage = ImageOps.fit(image, (width, height))
fittedimage.paste(shirt, shirt)

fittedimage.save(sys.argv[2])
