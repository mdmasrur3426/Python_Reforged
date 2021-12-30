def factorial(num: int) -> int:
    """
    Return factorial of the number
    :param num: Input number to calculate factorial
    :return: return factorial of a number
    """
    first_num = 1

    for number in range(1, num + 1):
        first_num *= number

    return first_num


for i in range(36):
    print(i, factorial(i))
