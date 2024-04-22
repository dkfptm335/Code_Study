def dfs(startNode, visit):
    global answer
    answer = max(answer, len(visit))

    for node in adjList[startNode]:
        if node not in visit:
            dfs(node, visit + [node])


t = int(input().strip())
for tc in range(1, t + 1):
    n, m = map(int, input().strip().split())
    adjList = [[] for _ in range(n + 1)]
    for _ in range(m):
        start, end = map(int, input().strip().split())
        adjList[start].append(end)
        adjList[end].append(start)

    answer = 0

    for i in range(1, n + 1):
        dfs(i, [i])

    print(f"#{tc} {answer}")
    