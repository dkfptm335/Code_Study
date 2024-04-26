import sys

n = int(sys.stdin.readline())
s, e = 1, 1
tmpSum = 1
count = 1

while e != n:
    if tmpSum < n:
        e += 1
        tmpSum += e
    elif tmpSum > n:
        tmpSum -= s
        s += 1
    else:
        count += 1
        e += 1
        tmpSum += e

print(count)
