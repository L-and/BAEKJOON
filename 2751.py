num_list_len = int(input())
num_list = list()

for i in range(num_list_len):
    temp = input()
    num_list.append(temp)

for i in range(num_list_len):
        for j in range(i + 1, num_list_len):
            if num_list[i] > num_list[j]:
                temp = num_list[i]
                num_list[i] = num_list[j]
                num_list[j] = temp

for i in range(num_list_len):
    print(num_list[i])