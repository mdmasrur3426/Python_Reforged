for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubes is {2:4}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubes is {2:^4}".format(i, i ** 2, i ** 3))