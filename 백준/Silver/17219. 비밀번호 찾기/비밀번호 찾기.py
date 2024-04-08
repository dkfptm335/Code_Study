import sys

n, m = map(int, sys.stdin.readline().strip().split())
passwords = {}
for _ in range(n):
    site, password = sys.stdin.readline().strip().split()
    passwords[site] = password

questions = [sys.stdin.readline().strip() for _ in range(m)]
answers = []

for question in questions:
    answers.append(passwords[question])

for answer in answers:
    print(answer)
