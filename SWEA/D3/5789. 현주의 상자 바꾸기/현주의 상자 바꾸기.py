t = int(input())

for tc in range(1, t + 1):
    n, q = map(int, input().strip().split())
    ranges = [list(map(int, input().strip().split())) for _ in range(q)]
    boxes = [0] * n

    for i in range(q):
        for j in range(ranges[i][0] - 1, ranges[i][1]):
            boxes[j] = i + 1

    print(f"#{tc} {' '.join(list(map(str, boxes)))}")
    