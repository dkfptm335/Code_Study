from collections import Counter

word = input()

cnt = Counter(word.lower())

if (list(cnt.values()).count(max(cnt.values())) > 1):
    print("?")
else:
    print(cnt.most_common(1)[0][0].upper())
