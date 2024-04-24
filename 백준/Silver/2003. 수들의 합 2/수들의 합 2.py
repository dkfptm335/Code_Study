import sys

N, M = map(int, sys.stdin.readline().strip().split())
numbers = list(map(int, sys.stdin.readline().strip().split()))

start, end = 0, 1
count = 0

while start <= end <= N:
    total = sum(numbers[start:end])
    if total == M:
        count += 1
        start += 1
    elif total < M:
        end += 1
    else:
        start += 1

print(count)
