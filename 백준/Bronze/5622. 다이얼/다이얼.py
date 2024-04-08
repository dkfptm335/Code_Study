import sys

times = {i: i + 1 for i in range(1, 10)}
times[0] = 11
alphabets = ['OPERATOR', ' ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

s = sys.stdin.readline().strip()
sNum = []
time = 0

for char in s:
    for i in range(2, 10):
        if char in alphabets[i]:
            sNum.append(i)

for num in sNum:
    time += times[num]

print(time)
