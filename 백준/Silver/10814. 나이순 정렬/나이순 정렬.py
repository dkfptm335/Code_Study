import sys

T = int(sys.stdin.readline().strip())
users = {}

for i in range(1, T+1):
    age, name = sys.stdin.readline().strip().split()
    age = int(age)
    users[i] = (age, name)

users = sorted(users.items(), key=lambda x: x[1][0])

for user in users:
    print(user[1][0], user[1][1])