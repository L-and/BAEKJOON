case = int(input())

for i in range(case):
    floors, rooms, N = input().split()
    floors = int(floors)
    rooms = int(rooms)
    N = int(N)

    if floors == 1:
        answer = 100 + N
    elif rooms == 1:
        answer = 100 * N + 1
    elif floors == N:
        answer = floors * 100 + 1
    else:
        answer = int((N % floors) * 100 + (N / floors) + 1)

    print(answer)