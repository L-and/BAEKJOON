from collections import deque

def bfs(x, y):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    count_of_house = 0

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        count_of_house += 1

        # 4빙향 확인
        for i in range(n):

            # 범위를 벗어났으면 continue
            if


n = int(input())

graph = []
visited = [[False for j in range(n)] for i in range(n)]
HouseNumList = []

for i in range(n):
    graph.append(list(map(int, input())))

