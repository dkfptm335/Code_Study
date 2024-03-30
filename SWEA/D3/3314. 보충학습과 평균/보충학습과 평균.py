t = int(input())

for tc in range(1, t + 1):
    scores = list(map(int, input().split()))

    for i in range(len(scores)):
        if scores[i] < 40:
            scores[i] = 40

    print(f"#{tc} {int(sum(scores) / len(scores))}")
