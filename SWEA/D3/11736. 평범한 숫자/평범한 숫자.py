t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().strip().split()))

    generalNum = 0

    for i in range(1, len(arr) - 1):
        if arr[i] != max(arr[i - 1], arr[i], arr[i + 1]) and arr[i] != min(arr[i - 1], arr[i], arr[i + 1]):
            generalNum += 1

    print(f"#{tc} {generalNum}")
