import sys
from math import sqrt

t = int(sys.stdin.readline().strip())
answers = []
for tc in range(1, t + 1):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().strip().split())
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # 1. 두 원이 일치하는 경우
    if distance == 0 and r1 == r2:
        answers.append(-1)
    # 3. 두 원이 내접하는 경우
    elif distance == abs(r1 - r2) or distance == r1 + r2:
        answers.append(1)
    # 4. 두 원이 두 점에서 만나는 경우
    elif abs(r1 - r2) < distance < r1 + r2:
        answers.append(2)
    # 6. 두 원이 외부에서 만나지 않는 경우
    else:
        answers.append(0)

for answer in answers:
    print(answer)
