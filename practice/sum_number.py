def sum_numbers(*values: float) -> float:
    """
    This function will return sum of all the variables
    :param values: numbers
    :return: sum of all numbers
    """
    return sum(values)


x = sum_numbers(1, 2, 3, 10)
print(x)
