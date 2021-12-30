def multiply(x: float, y: float) -> float:
    """
    Multiply two `variables.

    This function will multiply 2 `int`
    :param x: first `variable
    :param y: second `variable
    :return: The multiplication of 2 parameters.
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Check to see if the string input is a palindrome.

    :param string: The string that the function will check.
    :return: Return if the string is a palindrome or not.
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    Check to see if the sentence is a palindrome.
    :param sentence: The sentence that the function will check.
    :return: Return if the sentence is a palindrome or not.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

p = palindrome_sentence()
