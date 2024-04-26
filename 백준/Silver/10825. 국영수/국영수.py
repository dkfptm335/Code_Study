import sys

N = int(sys.stdin.readline())
students = dict()
for _ in range(N):
    scoreInput = sys.stdin.readline().strip().split()
    students[scoreInput[0]] = list(map(int, scoreInput[1:]))

students = sorted(students.items(), key=lambda x: (-x[1][0], x[1][1], -x[1][2], x[0]))
for student in students:
    print(student[0])
