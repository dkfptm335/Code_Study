import sys

colorPapers = int(sys.stdin.readline().strip())
paper = [[0] * 100 for _ in range(100)]
coordinates = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(colorPapers)]
for coordinate in coordinates:
    x, y = coordinate
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

colorArea = 0

for row in paper:
    colorArea += row.count(1)

print(colorArea)
