from operator import itemgetter

user_list = []

userCount = int(input())

for i in range(userCount):
    age, name = input().split()
    user_list.append((int(age), str(name)))

user_list = sorted(user_list, key=lambda user: user[0])

for i in range(userCount):
    print(user_list[i][0], user_list[i][1])

