T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().strip().split()))
    sumArr = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                sumArr.append(arr[i] + arr[j] + arr[k])

    sumArr = sorted(set(sumArr), reverse=True)
    print(f"#{tc} {sumArr[4]}")
    