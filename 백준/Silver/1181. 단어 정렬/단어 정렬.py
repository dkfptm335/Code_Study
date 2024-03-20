N = int(input())

words = []
for i in range(N):
    words.append(input())

words = list(set(words))
words.sort()
words.sort(key=len)

for word in words:
    print(word)