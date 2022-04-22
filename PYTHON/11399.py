n = int(input()) # 사람의 수
p = list(map(int, input().split())) # 개인당 ATM사용에 걸리는 시간

p.sort() # 오름차순으로 정렬
totalTime = 0

for i in range(n):
    totalTime += sum(p)
    del p[-1]

print(totalTime) # 결과 출력

##########

#Pi ~ Pm까지 마지막원소값을 제외해가며 모두 더하는식으로 해결