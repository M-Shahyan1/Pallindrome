"""
Tests the palindrome module
"""
from collections import deque
from palindrome import is_palindrome

def test_palindrome_check():
    assert is_palindrome(321) == ValueError
