import sys

N = int(sys.stdin.readline().strip())
times = list(map(int, sys.stdin.readline().strip().split()))
times.sort()
timeSum = 0

for i in range(len(times)):
    tmpTimes = times[:i + 1]
    timeSum += sum(tmpTimes)

print(timeSum)
