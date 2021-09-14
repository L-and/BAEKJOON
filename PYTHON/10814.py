user = []

userCount = int(input())

for i in range(userCount):
    age, name = map(str, input().split())
    user.append(name)

user.sort()

print(user)

