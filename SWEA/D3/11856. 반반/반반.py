t = int(input())

for tc in range(1, t + 1):
    testCase = list(input())
    if len(set(testCase)) == 2:
        if testCase.count(testCase[0]):
            print(f"#{tc} Yes")
        else:
            print(f"#{tc} No")
    else:
        print(f"#{tc} No")
