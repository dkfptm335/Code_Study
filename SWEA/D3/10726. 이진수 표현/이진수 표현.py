t = int(input())

for tc in range(1, t + 1):
    N, M = map(int, input().strip().split())
    result = ''

    # 총 길이가 N보다 작은 경우
    if len(bin(M)[2:]) < N:
        result = 'OFF'

    else:
        if (bin(M)[2:])[-N:].count('1') == N:
            result = 'ON'
        else:
            result = 'OFF'

    print(f"#{tc} {result}")
    