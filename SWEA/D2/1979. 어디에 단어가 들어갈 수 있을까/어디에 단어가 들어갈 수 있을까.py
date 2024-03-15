T = int(input())
test_cases = {}

for i in range(1, T+1):
    N, K = map(int, input().split())
    target = '1' * K
    count = 0

    arr = [input().split() for _ in range(N)]

    horizontal = []
    for row in arr:
        horizontal.append("".join(row).split('0'))

    arr_trans = []
    for j in range(N):
        tmp = []
        for k in range(N):
            tmp.append(arr[k][j])
        arr_trans.append(tmp)

    vertical = []
    for row in arr_trans:
        vertical.append("".join(row).split('0'))

    for row in vertical:
        count += row.count(target)
    for row in horizontal:
        count += row.count(target)

    test_cases[i] = count

for key, value in test_cases.items():
    print(f'#{key} {value}')