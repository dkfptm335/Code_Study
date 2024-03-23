import sys


N, M = map(int, input().split())
A = list(map(int, input().split()))

# A에서 카드 3장을 뽑아 만들 수 있는 모든 경우의 수를 구한다.
result = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            result.append(A[i] + A[j] + A[k])

# 각 경우의 수에 대해 M을 넘지 않는 가장 큰 수를 찾는다.
result.sort()
answer = 0
for r in result:
    if r <= M:
        answer = r
    else:
        break

print(answer)