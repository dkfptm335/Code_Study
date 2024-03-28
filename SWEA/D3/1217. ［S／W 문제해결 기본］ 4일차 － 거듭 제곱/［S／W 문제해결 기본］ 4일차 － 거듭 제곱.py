def multiple(n, m):
    if m == 0:
        return 1

    return n * multiple(n, m - 1)


for tc in range(1, 11):
    testNumber = int(input())
    n, m = map(int, input().split())

    print(f"#{tc} {multiple(n, m)}")