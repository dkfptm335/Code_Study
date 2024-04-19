import sys


x = int(sys.stdin.readline().strip())
num = 0
while x - num >= 0:
    x -= num
    num += 1

if x == 0:
    if num % 2 == 0:
        print(f"1/{num - 1}")
    else:
        print(f"{num - 1}/1")

else:
    if num % 2 == 0:
        print(f"{x}/{num + 1 - x}")
    else:
        print(f"{num + 1 - x}/{x}")
