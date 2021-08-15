from collections import 

def can_attack_check(x_list, y_list, n):
    for i in range(n):
        for j in range(n):
            if x_list[i] == x_list[j] or y_list[i] == y_list[j]:
                return True
            if x_list[i] - x_list[j] == y_list[i] - y_list[j]:
                return True

    return False


def bfs(graph, visited):

j
n = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]
visited = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]

board[0] = [1] * n  # 퀸들의 초기위치 세팅

