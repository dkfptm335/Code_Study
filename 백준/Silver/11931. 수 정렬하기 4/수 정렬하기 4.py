import sys

n = int(sys.stdin.readline().strip())
numbers = sorted([int(sys.stdin.readline().strip()) for _ in range(n)], reverse=True)
for number in numbers:
    print(number)
