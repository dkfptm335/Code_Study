from collections import deque

graph = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2, 4, 5],
    4: [3],
    5: [3]
}

visited = deque()
stack = deque()

def dfs(graph, start_node):
    stack.append(start_node)

    while stack:
        currentNode = stack.pop()

        if currentNode not in visited:
            visited.append(currentNode)

            for node in graph[currentNode]:
                dfs(graph, node)

    return visited

print(dfs(graph, 1))

