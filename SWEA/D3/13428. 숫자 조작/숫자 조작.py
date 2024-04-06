def swap(s, a, b):
    s = list(s)
    s[a], s[b] = s[b], s[a]
    return ''.join(s)


t = int(input())

for tc in range(1, t + 1):
    n = input()
    pairs = list()
    swapped = [int(n)]
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            pairs.append((i, j))

    for pair in pairs:
        tmp = swap(n, pair[0], pair[1])
        if not tmp.startswith('0'):
            swapped.append(int(tmp))

    swapped = sorted(set(swapped))
    if not swapped:
        swapped.append(0)

    print(f"#{tc} {swapped[0]} {swapped[-1]}")
