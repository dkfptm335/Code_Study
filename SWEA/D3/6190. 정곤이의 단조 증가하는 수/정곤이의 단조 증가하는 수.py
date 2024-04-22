def isMonotonicIncreaseNumber(num):
    tmp = list(map(int, list(str(num))))
    for k in range(len(tmp) - 1):
        if tmp[k] > tmp[k + 1]:
            return False
    return True


t = int(input().strip())
for tc in range(1, t + 1):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    maxArr = -1
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            tmpArr = arr[i] * arr[j]
            if isMonotonicIncreaseNumber(tmpArr):
                if maxArr < tmpArr:
                    maxArr = tmpArr

    print(f"#{tc} {maxArr}")
