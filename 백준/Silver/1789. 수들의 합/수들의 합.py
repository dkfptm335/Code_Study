import sys

s = int(sys.stdin.readline().strip())
tmpSum = 0
n = 0
for i in range(1, s):
    if tmpSum <= s:
        tmpSum += i

    if tmpSum > s:
        print(i - 1)
        break

if s == 1 or s == 2:
    print(1)
if s == 3:
    print(2)
    