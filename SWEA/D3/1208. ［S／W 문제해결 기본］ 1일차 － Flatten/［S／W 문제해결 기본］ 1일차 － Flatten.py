def dump(heights):
    maxHeight = max(heights)
    minHeight = min(heights)

    heights[heights.index(maxHeight)] -= 1
    heights[heights.index(minHeight)] += 1


for tc in range(1, 11):
    dumpCount = int(input())
    boxHeights = list(map(int, input().strip().split()))

    for _ in range(dumpCount):
        dump(boxHeights)

    print(f"#{tc} {max(boxHeights) - min(boxHeights)}")
