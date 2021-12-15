name = input("What is your name: ")
age = int(input("What is your age: "))

if 18 <= age <= 30:
    print("Welcome {} to the holiday club".format(name))
else:
    print("Hi {}, your are not eligible for the holiday".format(name))