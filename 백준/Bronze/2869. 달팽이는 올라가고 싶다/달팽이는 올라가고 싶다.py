import sys


A, B, V = map(int, sys.stdin.readline().split())
day = 0

if (V - A) % (A - B) == 0:
    day = (V - A) // (A - B)
else:
    day = (V - A) // (A - B) + 1

print(day + 1)