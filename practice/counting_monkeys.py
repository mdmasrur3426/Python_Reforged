n = int(input("How many monkeys?: "))
monkey = 1
counting_monkey = []

while monkey < n + 1:
    counting_monkey.append(monkey)
    monkey += 1
print(counting_monkey)