T = int(input())

for tc in range(1, T + 1):
    D, H, M = map(int, input().strip().split())
    diff = (D - 11) * 24 * 60 + (H - 11) * 60 + (M - 11)
    if diff < 0:
        print(f"#{tc} -1")
    else:
        print(f"#{tc} {diff}")
        