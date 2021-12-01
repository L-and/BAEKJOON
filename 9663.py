def promising(x, y):




def dfs(graph, visited):




n = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]
visited = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]

board[0] = [1] * n  # 퀸들의 초기위치 세팅

