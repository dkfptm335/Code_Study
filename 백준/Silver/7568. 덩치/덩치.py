import sys


humans = []
ranks = []

N = int(sys.stdin.readline())

for i in range(N):
    height, weight = map(int, sys.stdin.readline().split())
    humans.append((height, weight))

for i in range(N):
    rank = 1
    for j in range(N):
        if i == j:
            continue
        if humans[i][0] < humans[j][0] and humans[i][1] < humans[j][1]:
            rank += 1
    ranks.append(rank)

for rank in ranks:
    print(rank, end=' ')