t = int(input().strip())
for tc in range(1, t + 1):
    n, m = map(int, input().strip().split())
    firstSet = set(input().strip().split())
    secondSet = set(input().strip().split())
    intersectionSet = firstSet.intersection(secondSet)

    print(f"#{tc} {len(intersectionSet)}")
    