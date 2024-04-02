t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    # uni + twin = m
    # uni + twin * 2 = n

    twin = n - m
    uni = 2 * m - n

    print(f"#{tc} {uni} {twin}")
    