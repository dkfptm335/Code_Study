from collections import deque

t = int(input().strip())
for tc in range(1, t + 1):
    # n명의 손님, m초마다 k개의 붕어빵
    n, m, k = map(int, input().strip().split())
    people = deque(sorted(list(map(int, input().strip().split()))))
    demand = 0
    time = 0
    bread = 0
    count = 0
    isPossible = True

    while people:
        # 현재 시간에 방문 예정인 손님이 있는가?
        if people[0] == time:
            # 있다면 얼마나 있는가?
            demand += people.count(time)

        # 예상 수요 확인 후 방문 예정인 손님 대기열에서 제거
        while people and people[0] == time:
            people.popleft()

        # m초마다 주기 확인
        if count == m:
            count -= m
            bread += k

        if demand > bread:
            isPossible = False
            break

        # 시간 증가
        time += 1
        count += 1

    print(f"#{tc} {'Possible' if isPossible else 'Impossible'}")
