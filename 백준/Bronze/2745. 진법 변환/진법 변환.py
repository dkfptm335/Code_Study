import sys

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphaDict = {value: idx + 10 for idx, value in enumerate(alphabets)}

N, B = sys.stdin.readline().strip().split()
B = int(B)


result = 0
N = list(reversed(list(N)))
for i in range(len(N)):
    if N[i].isalpha():
        result += alphaDict[N[i]] * (B ** i)
    else:
        result += int(N[i]) * (B ** i)

print(result)
