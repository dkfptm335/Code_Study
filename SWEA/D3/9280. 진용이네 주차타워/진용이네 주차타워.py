from collections import deque

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().strip().split())
    parkingLot = [0] * n
    prices = [0] * n
    weights = [0] * m
    for i in range(n):
        prices[i] = int(input().strip())
    for i in range(m):
        weights[i] = int(input().strip())

    order = deque()
    for _ in range(2 * m):
        order.append(int(input().strip()))

    waitingLot = deque()

    total = 0

    while order:
        car = order.popleft()
        if car > 0:  # 입차

            # 자리가 있다면
            if 0 in parkingLot:
                currentPark = parkingLot.index(0)
                parkingLot[currentPark] += car
                total += prices[currentPark] * weights[car - 1]

            # 자리가 없다면
            else:
                waitingLot.append(car)

        else:  # 출차
            currentPark = parkingLot.index(-car)
            parkingLot[currentPark] += car
            if waitingLot:
                car = waitingLot.popleft()
                parkingLot[currentPark] = car
                total += prices[currentPark] * weights[car - 1]

    print(f"#{tc} {total}")
    