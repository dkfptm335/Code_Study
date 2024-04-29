from itertools import combinations

T = int(input().strip())
answers = []
for tc in range(1, T + 1):
    N, K = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    count = 0

    for i in range(1, N + 1):
        for data in combinations(A, i):
            if sum(data) == K:
                count += 1

    answers.append(count)

for i in range(len(answers)):
    print(f"#{i + 1} {answers[i]}")
   