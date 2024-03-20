T = int(input())
test_cases = {}

for i in range(1, T+1):
    H, W, N = map(int, input().split())

    # 층 정하기: N % H
    # 호실 정하기 : N // H + 1
    # N % H == 0일 때는 H층에 배정
    floor = N % H
    room = N // H + 1
    if floor == 0:
        floor = H
        room = N // H

    test_cases[i] = str(floor) + str(room).zfill(2)

for i in range(1, T+1):
    print(test_cases[i])