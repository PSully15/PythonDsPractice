from turtle import forward


def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    forward = phrase.lower().replace(' ', '')
    return forward == forward[::-1]

# Return True/False if phrase is a palindrome
print(is_palindrome('tacocat'))  # True
print(is_palindrome('noon'))  # True
print(is_palindrome('robert'))  # False

# Should ignore capitalization/spaces when deciding
print(is_palindrome('taco cat'))  # True
print(is_palindrome('Noon'))  # True
