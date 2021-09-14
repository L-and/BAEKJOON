import sys

num_list_len = int(sys.stdin.readline())
num_list = list()

for i in range(num_list_len):
    num = int(sys.stdin.readline())
    if num in num_list:
        num_list[num_list.index(num)][1] += 1
    else:
        num_list.append((num, 1))

num_list.sort() 

for i in range(num_list_len):
    for j in range(num_list[i][1]):
        sys.stdout.write(str(num_list[i][0]) + '\n')

