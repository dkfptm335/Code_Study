T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    sizes = [int(input()) for _ in range(N)]
    sumSize = sum(sizes)
    count = 0
    for size in sizes:
        if size > sumSize / N:
            count += size - sumSize / N

    print(f"#{tc} {int(count)}")
    