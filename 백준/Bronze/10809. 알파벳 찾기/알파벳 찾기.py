S = input()

# 97 ~ 122

isin = []

for i in range(97, 123):
    isin.append(S.find(chr(i)))

print(' '.join(map(str, isin)))