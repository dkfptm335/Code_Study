T = int(input())

test_cases = {i: [] for i in range(1, T+1)}

for i in range(1, T+1):
    N = int(input())
    arr = []
    for j in range(N):
        arr.append(list(map(int, input().split())))

    for j in range(N):
        tmp_90 = ''
        for k in range(N):
            tmp_90 += str(arr[k][j])
        tmp_90 = tmp_90[::-1]
        test_cases[i].append([tmp_90])

    for j in range(N-1, -1, -1):
        tmp_180 = ''
        for k in range(N-1, -1, -1):
            tmp_180 += str(arr[j][k])
        test_cases[i][N-1-j].append(tmp_180)

    for j in range(N):
        tmp_270 = ''
        for k in range(N-1, -1, -1):
            tmp_270 += str(arr[k][j])
        tmp_270 = tmp_270[::-1]
        test_cases[i][N-1-j].append(tmp_270)

for i in range(1, T+1):
    print(f'#{i}')
    for j in range(len(test_cases[i])):
        print(*test_cases[i][j])