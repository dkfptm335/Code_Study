import sys

n = list(map(int, list(sys.stdin.readline().strip())))
numDict = {i: 0 for i in range(10)}
for num in n:
    numDict[num] += 1

maxOfExceptSixAndNine = 0
sumOfSixAndNine = 0
for k, v in numDict.items():
    if k == 6 or k == 9:
        sumOfSixAndNine += v
    else:
        maxOfExceptSixAndNine = max(maxOfExceptSixAndNine, v)

if sumOfSixAndNine % 2 == 0:
    sumOfSixAndNine //= 2
else:
    sumOfSixAndNine = sumOfSixAndNine // 2 + 1

print(max(maxOfExceptSixAndNine, sumOfSixAndNine))
