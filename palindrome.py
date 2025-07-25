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
        word = word.upper()
        pass

    dequed_word = deque(word)
    if len(dequed_word) < 1:
        return False

    elif len(dequed_word) == 1:
        return True

    else:
        beginning = dequed_word.popleft()
        end = dequed_word.pop()
        if beginning != end:
            return False
        else:
            return True
            pass
        pass

