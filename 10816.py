import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

## 입력 ##

len_of_card = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

len_of_target_card = int(sys.stdin.readline())

target_card = list(map(int, sys.stdin.readline().split()))

card.sort() # binary search 를 쓰기위해 정렬

current_target_index = 0 #현재 목표카드의 인덱스
num_of_target_card = [0 for i in range(len_of_target_card)] # 찾은 타겟카드의 개수
completion_target_num = [] # 이미 찾은 타겟카드

while current_target_index < len(target_card):
    if target_card[current_target_index] in completion_target_num:
        num_of_target_card[current_target_index] = num_of_target_card[target_card.index(target_card[current_target_index])]
        current_target_index = current_target_index + 1

    target_index = binary_search(card, target_card[current_target_index], 0, len(card) - 1)
#   찾은 목표카드의 인덱스
    if target_index is not None:
        num_of_target_card[current_target_index] = num_of_target_card[current_target_index] + 1
        del card[target_index]
    else:
        completion_target_num.append(target_card[current_target_index])
        current_target_index = current_target_index + 1
## 결과 출력

print(" ".join(str(num_of_target_card[i]) for i in range(len_of_target_card)))