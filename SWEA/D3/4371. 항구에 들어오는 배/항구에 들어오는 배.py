from collections import deque

t = int(input().strip())
answers = []
for tc in range(t):
    n = int(input().strip())
    happyDays = deque([int(input().strip()) - 1 for _ in range(n)][1:])
    ships = 0

    while happyDays:
        ships += 1
        tmp = happyDays.popleft()
        if happyDays:
            delIndexes = []
            for i in range(len(happyDays)):
                if happyDays[i] % tmp == 0:
                    delIndexes.append(i)

            for index in delIndexes[::-1]:
                del happyDays[index]

    answers.append(ships)

for i in range(len(answers)):
    print(f"#{i + 1} {answers[i]}")
