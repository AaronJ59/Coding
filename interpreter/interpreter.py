expression = input("What do you want solved? ")

x, y, z = expression.split(" ")

if y == "+":
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "*":
    print(float(x) * float(z))
elif y == "/":
    print(float(x) / float(z))
else:
    print("Try +, -, *, /")