import sys


def isHansu(n):
    if len(str(n)) == 1 or len(str(n)) == 2:
        return True
    else:
        for i in range(len(str(n)) - 2):
            if int(str(n)[i + 1]) - int(str(n)[i]) != int(str(n)[i + 2]) - int(str(n)[i + 1]):
                return False

        return True


n = int(sys.stdin.readline().strip())
count = 0
for num in range(1, n + 1):
    if isHansu(num):
        count += 1

print(count)
