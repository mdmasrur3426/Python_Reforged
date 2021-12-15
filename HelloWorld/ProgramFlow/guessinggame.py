import random

highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: remove after testing

print("Please guess number between 1 and {}: ".format(highest))
guess = 0

while guess != answer:
    guess = int(input())

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")
