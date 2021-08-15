from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for index, value in enumerate(graph[v]):
        if value == 1 and not visited[index]:
            dfs(graph, index, visited)

def bfs(graph, start, visited):
    queue = deque()

    queue.append(start)

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for index, value in enumerate(graph[v]):
            if value == 1 and not visited[index]:
                visited[index] = True
                queue.append(index)

    print('')


n, m, v = map(int, input().split())

graph = [[0 for i in range(n + 1)] for j in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())

    graph[x][y] = 1
    graph[y][x] = 1

dfs(graph, v, visited)
print('')
visited = [False] * (n + 1)
bfs(graph, v, visited)
