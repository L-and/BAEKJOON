test_case = int(input())
floors = int(input())
rooms = int(input())
# for case in range(test_case):
room = [[0 for col in range(floors)] for row in range(rooms)]

print(range(floors))

for i in range(floors):
    for j in range(rooms):
        print(room[i][j], end=' ')
    print()