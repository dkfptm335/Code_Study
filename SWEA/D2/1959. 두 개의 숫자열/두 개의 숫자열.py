T = int(input())
test_cases = {i: 0 for i in range(1, T+1)}

for i in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 최댓값
    max_sum = 0

    if N > M:
        for j in range(N-M+1):
            sum = 0
            for k in range(M):
                sum += A[j+k] * B[k]
            if sum > max_sum:
                max_sum = sum
    else:
        for j in range(M-N+1):
            sum = 0
            for k in range(N):
                sum += A[k] * B[j+k]
            if sum > max_sum:
                max_sum = sum

    test_cases[i] = max_sum

for i in range(1, T+1):
    print(f'#{i} {test_cases[i]}')