t = int(input().strip())
for tc in range(1, t + 1):
    # 버스 노선 n개
    n = int(input().strip())
    # i번째 버스 노선은 nList[i][0] 이상 nList[i][1] 이하인 모든 정류장을 다니는 버스 노선
    nList = [list(map(int, input().strip().split())) for _ in range(n)]
    p = int(input().strip())
    # p개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지?
    pList = [int(input().strip()) for _ in range(p)]
    pDict = {i: 0 for i in set(pList)}

    for stops in nList:
        a, b = stops
        for k in pDict.keys():
            if a <= k <= b:
                pDict[k] += 1

    print(f"#{tc}", end=' ')
    for num in pList:
        print(pDict[num], end=' ')
    print()
