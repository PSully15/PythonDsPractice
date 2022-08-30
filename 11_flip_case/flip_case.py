def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    to_swap = to_swap.lower()
    final_phrase = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        final_phrase += ltr
    return final_phrase


print(flip_case('Aaaahhh', 'a'))  # aAAAhhh
print(flip_case('Aaaahhh', 'A'))  # aAAAhhh
print(flip_case('Aaaahhh', 'h'))  # AaaaHHH
