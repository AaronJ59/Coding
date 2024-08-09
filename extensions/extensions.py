file = input("What's the name of the file? ")
jfiles = ".jpeg",".jpg"

if file.casefold().strip().endswith(".gif"):
    print("image/gif")
elif file.casefold().strip().endswith(jfiles):
    print("image/jpeg")
elif file.casefold().strip().endswith(".png"):
    print("image/png")
elif file.casefold().strip().endswith(".pdf"):
    print("application/pdf")
elif file.casefold().strip().endswith(".txt"):
    print("text/plain")
elif file.casefold().strip().endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")