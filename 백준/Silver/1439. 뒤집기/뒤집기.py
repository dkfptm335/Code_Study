import sys

n = sys.stdin.readline().strip()
start = 0
parsedN = []
tmp = ''
for i in range(len(n) - 1):
    tmp += n[i]
    if n[i] != n[i + 1]:
        parsedN.append(tmp)
        tmp = ''

tmp += n[-1]
parsedN.append(tmp)
zeroCount = 0
oneCount = 0
for s in parsedN:
    if s.startswith("0"):
        zeroCount += 1
    else:
        oneCount += 1

print(min(zeroCount, oneCount))
