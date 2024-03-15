import sys
sys.setrecursionlimit(1000000)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

N = int(input())
print(1 if N == 0 else factorial(N))