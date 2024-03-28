t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())
    number = list(map(int, input().split()))

    notSubmitted = []

    for i in range(1, n + 1):
        if i not in number:
            notSubmitted.append(i)

    notSubmitted.sort()

    print(f"#{tc} {' '.join(map(str, notSubmitted))}")