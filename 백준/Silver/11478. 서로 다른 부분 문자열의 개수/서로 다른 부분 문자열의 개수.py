import sys

S = sys.stdin.readline().strip()
subStrings = []
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        subStrings.append(S[i: j])

subStrings = set(subStrings)
print(len(subStrings))
