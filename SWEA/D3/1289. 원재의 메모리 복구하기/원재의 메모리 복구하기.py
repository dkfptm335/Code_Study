def reviseMemory(memory, idx, bit):
    memoryList = list(memory)

    for i in range(idx, len(memoryList)):
        memoryList[i] = bit

    return ''.join(memoryList)


T = int(input())


for tc in range(1, T + 1):
    origMemory = input()
    memory = "0" * len(origMemory)

    count = 0

    while origMemory != memory:
        for i in range(len(origMemory)):
            if origMemory[i] != memory[i]:
                memory = reviseMemory(memory, i, origMemory[i])
                count += 1
                break

    print(f"#{tc} {count}")