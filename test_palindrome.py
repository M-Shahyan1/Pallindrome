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

def test_forgotten_palindrome():
    assert is_palindrome("bb") == True

def test_non_palindrome():
    assert is_palindrome("abc") == False

def test_singular_palindrome():
    assert is_palindrome("laval") == True

def test_complex_nonpalindrome():
    assert is_palindrome("toronto") == False

def test_complex_palindrome():
    assert is_palindrome("Able was I ere I saw Elba") == True
