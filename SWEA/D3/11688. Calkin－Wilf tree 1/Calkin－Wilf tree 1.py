def modifyMemory(memory, idx, bit):
    memoryList = list(memory)

    for i in range(idx, len(memoryList)):
        memoryList[i] = bit

    return ''.join(memoryList)


T = int(input())


for tc in range(1, T + 1):
    logs = list(input())
    node = [1, 1]  # [numerator, denominator], root node

    for log in logs:
        if log == 'L':
            node[1] += node[0]
        else:
            node[0] += node[1]

    print(f"#{tc} {node[0]} {node[1]}")
