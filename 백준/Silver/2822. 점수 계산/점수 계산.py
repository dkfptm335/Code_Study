import sys

scoreDict = {i: int(sys.stdin.readline().strip()) for i in range(1, 9)}
scoreDict = sorted(scoreDict.items(), key=lambda x: x[1], reverse=True)
result = []
score = 0
for k, v in scoreDict:
    if not len(result) == 5:
        result.append(k)
        score += v

result.sort()
print(score)
print(' '.join(map(str, result)))
