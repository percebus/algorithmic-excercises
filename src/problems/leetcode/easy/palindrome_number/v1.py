# SRC: https://leetcode.com/problems/palindrome-number/
#
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.


def is_palindrome(number: int) -> bool:
    str1 = str(number)
    str2 = str1[::-1]
    return str1 == str2
