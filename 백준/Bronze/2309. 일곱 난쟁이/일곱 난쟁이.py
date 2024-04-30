import sys
from itertools import combinations

answers = []

heights = [int(sys.stdin.readline().strip()) for _ in range(9)]
for value in combinations(heights, 7):
    if sum(value) == 100:
        answers = list(value)
        break

for num in sorted(answers):
    print(num)
