N, M = map(int, input().split())

square = [[0 for j in range(M)] for i in range(N)]

for i in range(N):
    square[i] = input()

for i in range(N):
    for j in range(M):
        print(square[i][j], end=' ')
    print()