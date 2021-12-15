dial_input = "-"
while dial_input != "0":
    if dial_input in "12345":
        print("The option you selected is {}".format(dial_input))
    else:
        print("lease choose your option from the list below:")
        print("1: \tLearn Python")
        print("2: \tLearn Java")
        print("3: \tLearn Python")
        print("4: \tLearn Python")
        print("5: \tLearn Python")
        print("0: \tExit")

    dial_input = input()