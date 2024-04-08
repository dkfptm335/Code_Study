import sys

A, B = sys.stdin.readline().split()
A = int(A[::-1])
B = int(B[::-1])

print(A if A > B else B)
