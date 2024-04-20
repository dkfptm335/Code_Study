import sys

n = int(sys.stdin.readline().strip())
logs = [sys.stdin.readline().strip().split() for _ in range(n)]
employee = dict()

for log in logs:
    a, b = log[0], log[1]
    employee[a] = b

result = []
for k, v in employee.items():
    if v == "enter":
        result.append(k)

result.sort(reverse=True)
for people in result:
    print(people)
    