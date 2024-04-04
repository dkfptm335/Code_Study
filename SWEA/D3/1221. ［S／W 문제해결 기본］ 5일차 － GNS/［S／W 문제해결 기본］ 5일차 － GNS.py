num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
numDict = {idx: value for idx, value in enumerate(num)}
numDictReverse = {value: idx for idx, value in numDict.items()}
# print(numDict)
# print(numDictReverse)


t = int(input())

for tc in range(1, t + 1):
    testNum, n = input().strip().split()
    n = int(n)
    numbers = input().strip().split()

    for i in range(len(numbers)):
        numbers[i] = numDictReverse[numbers[i]]

    numbers.sort()
    for i in range(len(numbers)):
        numbers[i] = numDict[int(numbers[i])]

    print(f"#{tc}")
    print(' '.join(numbers))
    