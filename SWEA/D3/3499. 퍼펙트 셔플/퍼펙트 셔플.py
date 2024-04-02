from collections import deque


def myRound(n):
    n_decimal = n % 1
    if n_decimal >= 0.5:
        return int(n) + 1
    return int(n)


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    origin_cards = input().split()
    first = deque(origin_cards[:myRound(n / 2)])
    second = deque(origin_cards[myRound(n / 2):])
    result = []

    while len(result) != n:
        if len(first) != 0:
            result.append(first.popleft())
        if len(second) != 0:
            result.append((second.popleft()))

    print(f"#{tc} {' '.join(result)}")
