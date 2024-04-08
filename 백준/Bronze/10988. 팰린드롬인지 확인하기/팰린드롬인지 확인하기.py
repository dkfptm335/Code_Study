import sys


def is_palindrome(s):
    return s == s[::-1]


s = sys.stdin.readline().strip()
print(1 if is_palindrome(s) else 0)
