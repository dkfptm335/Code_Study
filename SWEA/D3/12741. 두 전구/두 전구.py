answer = []

t = int(input().strip())
for tc in range(1, t + 1):
    a, b, c, d = map(int, input().strip().split())
    set1 = set([i for i in range(a, b + 1)])
    set2 = set([i for i in range(c, d + 1)])
    intersectionSet = set1.intersection(set2)
    if len(intersectionSet) != 0:
        answer.append(len(intersectionSet) - 1)
    else:
        answer.append(len(intersectionSet))

for i in range(t):
    print(f"#{i + 1} {answer[i]}")
