import sys

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
numbers = sorted(list(set(numbers)))
print(' '.join(map(str, numbers)))
