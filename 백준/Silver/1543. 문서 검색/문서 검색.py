import sys

s = list(sys.stdin.readline().strip())
target = list(sys.stdin.readline().strip())
count = 0

for i in range(len(s) - len(target) + 1):
    if s[i:i + len(target)] == target:
        count += 1
        for j in range(i, i + len(target)):
            s[j] = "*"

print(count)
