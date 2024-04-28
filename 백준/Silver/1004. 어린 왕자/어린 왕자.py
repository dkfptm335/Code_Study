import sys


def isInSamePlanet(start, end, tmpPlanet):
    start_x, start_y = start
    end_x, end_y = end
    cx, cy, rx = tmpPlanet
    # (x - cx) ** 2 + (y - cy) ** 2 < rx ** 2
    if (start_x - cx) ** 2 + (start_y - cy) ** 2 < rx ** 2:
        if (end_x - cx) ** 2 + (end_y - cy) ** 2 < rx ** 2:
            return True
    return False


def isInPlanet(point, tmpPlanet):
    x, y = point
    cx, cy, rx = tmpPlanet
    if (x - cx) ** 2 + (y - cy) ** 2 < rx ** 2:
        return True
    return False


t = int(sys.stdin.readline().strip())
answers = []
for tc in range(1, t + 1):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    n = int(sys.stdin.readline().strip())
    planets = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    count = 0
    for planet in planets:
        if not isInSamePlanet([x1, y1], [x2, y2], planet):
            count += 1 if isInPlanet([x1, y1], planet) else 0
            count += 1 if isInPlanet([x2, y2], planet) else 0

    answers.append(count)

for answer in answers:
    print(answer)
