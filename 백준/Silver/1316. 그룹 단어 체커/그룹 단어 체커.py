import sys

N = int(sys.stdin.readline())
groupWord = 0
for i in range(N):
    word = sys.stdin.readline().strip()
    for char in word:
        if word.count(char) > 1:
            if char * word.count(char) not in word:
                break

    else:
        groupWord += 1

print(groupWord)
