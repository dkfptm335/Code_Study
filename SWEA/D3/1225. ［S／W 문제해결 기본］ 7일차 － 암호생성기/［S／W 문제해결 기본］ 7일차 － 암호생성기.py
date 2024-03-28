from collections import deque

for tc in range(1, 11):
    testNum = int(input())
    dataset = list(map(int, input().split()))
    deq = deque(dataset)
    isEnd = False

    while True:
        for i in range(1, 6):
            if deq[0] - i <= 0:
                deq.popleft()
                deq.append(0)
                isEnd = True
                break
            else:
                deq.append(deq.popleft() - i)

        if isEnd:
            break

    print(f"#{tc} {' '.join(map(str, list(deq)))}")
