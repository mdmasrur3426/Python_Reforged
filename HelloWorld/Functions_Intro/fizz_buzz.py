def fizz_buzz(num: int) -> str:
    """
    Play Fizz buzz
    :param num: The number to check.
    :return: Return the string
    """
    if num % 15 == 0:
        return "fizz buzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)


input("Play Fizz Buzz. Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
        print("you lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done, you reached {}".format(next_number))

