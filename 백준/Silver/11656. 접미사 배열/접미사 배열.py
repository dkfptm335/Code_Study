import sys

s = sys.stdin.readline().strip()
tails = []
for i in range(len(s)):
    tails.append(s[i:])
tails.sort()
for tail in tails:
    print(tail)
    