import sys

N, K = map(int, sys.stdin.readline().strip().split())
medalScoresDict = {i: list(map(int, sys.stdin.readline().strip().split())) for i in range(1, N + 1)}
medalScores = sorted(medalScoresDict.items(), key=lambda x: (-x[1][0], -x[1][1], -x[1][2]))
ranks = [1]
for i in range(1, N):
    if medalScores[i][1] == medalScores[i - 1][1]:
        ranks.append(ranks[-1])
    else:
        ranks.append(len(ranks) + 1)

print(ranks[medalScores.index((K, medalScoresDict[K]))])
