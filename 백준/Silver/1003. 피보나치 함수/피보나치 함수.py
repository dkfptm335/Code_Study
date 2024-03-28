import sys

t = int(sys.stdin.readline().strip())
for i in range(t):
    n = int(sys.stdin.readline().strip())
    a, b = 1, 0
    for j in range(n):
        a, b = b, a + b
    print(a, b)
