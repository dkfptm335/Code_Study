import sys


def binarySearch(target, array):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


n = int(sys.stdin.readline().strip())
sCards = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
isInScards = list(map(int, sys.stdin.readline().strip().split()))
result = []

sCards.sort()

for card in isInScards:
    if binarySearch(card, sCards) != -1:
        result.append("1")
    else:
        result.append("0")

print(' '.join(result))
