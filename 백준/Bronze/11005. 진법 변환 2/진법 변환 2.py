import sys

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphaDict = {value: idx + 10 for idx, value in enumerate(alphabets)}
newAlphaDict = {value: key for key, value in alphaDict.items()}

N, B = map(int, sys.stdin.readline().strip().split())
result = []

while N // B != 0:
    result.append(N % B)
    N //= B

result.append(N % B)
N //= B

result.reverse()
num = ''
for char in result:
    if char > 9:
        num += newAlphaDict[char]
    else:
        num += str(char)

print(num)
