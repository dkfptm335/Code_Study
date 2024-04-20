import sys

n, k = map(int, sys.stdin.readline().strip().split())
numbers = list(map(int, sys.stdin.readline().strip().split()))
print(list(sorted(numbers))[k - 1])
