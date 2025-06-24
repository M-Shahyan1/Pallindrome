"""
Validates strings as palindromes.
"""
from collections import deque

def is_palindrome(word):
    try:
        stringcheck = (word + 1)
        if stringcheck == word + 1:
            return ValueError
        pass
    except TypeError:
        pass

    dequed_word = deque(word)
    if len(dequed_word) < 1:
        return False

    elif len(dequed_word) == 1:
        return True

    else:
        pass

