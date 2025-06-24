"""
Tests the palindrome module
"""
from collections import deque
from palindrome import is_palindrome

def test_palindrome_check():
    assert is_palindrome(321) == ValueError

def test_blank_palindrome():
    assert is_palindrome('') == False

def test_single_palindrome():
    assert is_palindrome("a") == True

def test_non_palindrome():
    assert is_palindrome("abc") == False

