import sys

n = int(sys.stdin.readline().strip())
ropes = [int(sys.stdin.readline().strip()) for _ in range(n)]
ropes.sort(reverse=True)
answers = []
for i in range(n):
    answers.append((i + 1) * ropes[i])

print(max(answers))
