def palindrome_sentence(string):
    new_string = ''
    for letter in string:
        if letter.isalnum() or letter.isalpha():
            new_string += letter
        else:
            pass
    return new_string[::-1].casefold() == new_string.casefold()


word = input("Please enter a word to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))