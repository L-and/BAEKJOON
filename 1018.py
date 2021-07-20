N, M = map(int, input().split())

square = [[0 for j in range(M)] for i in range(N)]

for i in range(N):
    square[i] = input()

###############비교하기 위한 체스판 생성 ###############

white_board = [[0 for j in range(8)] for i in range(8)]
black_board = [[0 for j in range(8)] for i in range(8)]

current_color = 'W'

for i in range(8):
    for j in range(8):
        white_board[i][j] = current_color
        if current_color == 'W' and j != 7:
            current_color = 'B'
        elif current_color == 'B' and j != 7:
            current_color = 'W'

current_color = 'B'

for i in range(8):
    for j in range(8):
        black_board[i][j] = current_color
        if current_color == 'W' and j != 7:
            current_color = 'B'
        elif current_color == 'B' and j != 7:
            current_color = 'W'

###########################################

def compare_white_board(square, col, row):  # 흰색으로 시작하는 보드판과 비교
    answer = 0  # 같은 색의 수
    for i in range(8):
        for j in range(8):
            if square[col + i][row + j] == white_board[i][j]:
                answer = answer + 1
    return answer

def compare_black_board(square, col, row):  # 검은색으로 시작하는 보드판과 비교
    answer = 0  # 같은 색의 수
    for i in range(8):
        for j in range(8):
            if square[col + i][row + j] == black_board[i][j]:
                answer = answer + 1
    return answer

max_same = 0
current_same = 0

for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        current_same = compare_black_board(square, i, j)
        if current_same < compare_white_board(square, i, j):
            current_same = compare_white_board(square, i, j)

        if current_same > max_same:
            max_same = current_same

    #     print(current_same, end=' ')
    # print()

print(64 - max_same)