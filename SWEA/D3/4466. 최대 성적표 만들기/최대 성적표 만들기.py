t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())
    scores = sorted(list(map(int, input().split())), reverse=True)

    max_score = sum(scores[:k])

    print(f"#{tc} {max_score}")
    