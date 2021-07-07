case = int(input())

for loop in range(case):
    start_point, end_point = input().split()
    start_point = int(start_point)
    end_point = int(end_point)

    distance = end_point - start_point # 이동해야 할 거리

    current_distance = 0 # 현재 이동한 거리
    
    k = 1 # 현재 이동가능한 거리

    num_of_operation = 0
    
    while distance >= current_distance:
        current_distance = current_distance + k
        k = k + 1
        num_of_operation = num_of_operation + 1

    print(num_of_operation)
