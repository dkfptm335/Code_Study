K, N = map(int, input().split())

Lan = [int(input()) for _ in range(K)]

total_len = sum(Lan)
start, end = 1, total_len // N

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for l in Lan:
        cnt += l // mid
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)