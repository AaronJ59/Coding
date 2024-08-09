s = input("Do you agree? ").lower()

if s in ["y", "yes"]:
    print("Agreed")
elif s in ["n", "no"]:
    print("Not agreed")

before = input("Before: ")
after = before.upper()
print(f"After: {after}")
print(f"After: {before.upper()}")


