import sys

L = int(sys.stdin.readline())
sentence = sys.stdin.readline().strip()
ascii_sentence = [ord(c)-96 for c in sentence]
sum_ascii = 0

for i in range(L):
    sum_ascii += ascii_sentence[i] * (31 ** i)

print(sum_ascii % 1234567891)
