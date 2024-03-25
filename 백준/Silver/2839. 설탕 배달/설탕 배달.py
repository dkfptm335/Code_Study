import sys


N = int(sys.stdin.readline())
ea = float('inf')

for i in range(0, N//3 + 1):
    for j in range(0, N//5 + 1):
        if 3*i + 5*j == N:
            if i+j < ea:
                ea = i+j

if ea == float('inf'):
    print(-1)
else:
    print(ea)