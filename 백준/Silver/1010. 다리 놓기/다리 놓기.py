import sys
from math import factorial


t = int(sys.stdin.readline().strip())
for tc in range(1, t + 1):
    n, m = map(int, sys.stdin.readline().strip().split())
    # m combination n
    bridge = factorial(m) / (factorial(n) * factorial(m - n))
    print(int(bridge))
