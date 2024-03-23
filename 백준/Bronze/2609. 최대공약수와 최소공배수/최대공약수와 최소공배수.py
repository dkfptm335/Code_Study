import sys


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


num1, num2 = map(int, sys.stdin.readline().split())

print(gcd(num1, num2))
print(lcm(num1, num2))
