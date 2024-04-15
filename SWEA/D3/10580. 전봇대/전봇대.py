from itertools import combinations


def isCrossed(line1, line2):
    if (line1[0] > line2[0] and line1[1] < line2[1]) or (line1[0] < line2[0] and line1[1] > line2[1]):
        return True
    return False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N)]
    crossedPoints = 0

    for combination in combinations(range(len(lines)), 2):
        if isCrossed(lines[combination[0]], lines[combination[1]]):
            crossedPoints += 1

    print(f"#{tc} {crossedPoints}")
