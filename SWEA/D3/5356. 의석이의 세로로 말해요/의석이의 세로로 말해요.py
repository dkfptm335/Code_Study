t = int(input())

for tc in range(1, t + 1):
    words = [input() for _ in range(5)]
    max_length = max([len(row) for row in words])
    for i in range(len(words)):
        words[i] = words[i].ljust(max_length, "*")

    words = list(map(list, zip(*words)))
    result = ''
    for word in words:
        for char in word:
            result += char

    result = result.replace("*", "")
    print(f"#{tc} {result}")
