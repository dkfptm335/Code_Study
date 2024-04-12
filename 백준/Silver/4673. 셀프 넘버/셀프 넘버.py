import sys

numbers = []


def func(n):
    return n + sum(map(int, str(n)))


num = 1
while True:
    if num > 10000:
        break
    numbers.append(func(num))
    num += 1

for i in range(1, 10001):
    if i not in numbers:
        print(i)