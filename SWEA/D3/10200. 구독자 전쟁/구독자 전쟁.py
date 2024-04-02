t = int(input())

for tc in range(1, t + 1):
    n, a, b = map(int, input().split())
    maxSubscriber = min(a, b)
    minSubscriber = 0 if a + b <= n else a + b - n

    print(f"#{tc} {maxSubscriber} {minSubscriber}")
