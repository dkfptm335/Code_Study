# BFS, 너비 우선 탐색 알고리즘
# 그래프를 탐색하는 알고리즘 중 하나로, 시작 정점으로부터 가까운 정점부터 탐색하는 알고리즘

# 예시 그래프 https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fd339L8%2FbtqZGm3MDjZ%2FkHOZmj27KLb56J9YXLXo5k%2Fimg.png

from collections import deque


# BFS 알고리즘 구현
def bfs(graph, node, visited):
    queue = deque([node])
    # 방문한 노드 체크
    visited[node] = True
    # 큐가 모두 빌 때까지 반복
    while queue:
        # 큐의 맨 앞에 있는 노드 꺼내기
        currentNode = queue.popleft()
        # 탐색 순서 출력
        print(currentNode, end = ' ')
        # 그래프에서 현재 탐색한 노드에 인접한 노드 중에서
        for i in graph[currentNode]:
            # 방문하지 않은 노드 탐색 후
            if not visited[i]:
                # 큐에 추가
                queue.append(i)
                # 해당 노드 방문 처리
                visited[i] = True
                
    return -1
    
def dfs(graph, node, visited):
    # 해당 노드 방문 처리
    visited[node] = True
    # 탐색 순서 출력
    print(node, end = ' ')
    # 인접한 다른 노드 재귀적으로 방문 처리
    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)
    return visited

# 딕셔너리 형태의 그래프
graph = {
    1: [2, 3],
    2: [1, 8],
    3: [1 ,4, 5],
    4: [3, 5],
    5: [3, 4],
    6: [7, 8],
    7: [6, 8],
    8: [2, 6, 7]
}

bfs_visited = {i: False for i in range(1, 9)}
dfs_visited = {i: False for i in range(1, 9)}
bfs(graph, 1, bfs_visited)
print()
dfs(graph, 1, dfs_visited)
