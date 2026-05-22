# name = input('Enter your name: ')
# age = int(input('Enter your age: '))
# height = float(input("Enter your height: "))


# print("Hello", name)
# print("you are", age, "years old")
# print("your height is", height, "feet")

name = input('Enter your name: ').strip()

if name == "":
    print("Cannot be empty")
    exit()

while True:
    try:
        age = int(input("Enter your age: "))

        if age < 0 or age > 120:
            print("Please enter a valid age (0-120)")
            continue

        break
    except ValueError:
        print("Please enter a valid age")

while True:
    try:
        height = float(input("Enter you height (in feet): "))
        if height < 0 or height > 8:
            print("Please enter a valid Height (0-8)")
            continue

        break
    except ValueError:
        print("Please enter a valid number for height")


print("\nHello", name)
print("You are", age, "year old")
print("Your height is", height, "feet" if height > 1 else "foot")
