t = int(input())
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, t + 1):
    m, d = map(int, input().split())
    dateDiff = 0

    if m == 1:
        dateDiff = d - 1

    else:
        dateDiff += sum(days[:m - 1])
        dateDiff += d - 1

    dateDiff = ((dateDiff % 7) + 4) % 7
    print(f"#{tc} {dateDiff}")
    