num_of_words = int(input())

words = list()
words_length = set()

# 단어입력
for i in range(num_of_words):
    word = input()
    words.append(word)
    words_length.add(len(word))

row = max(words_length)

# 2차원 리스트 생성
sorted_words = [[] for M in range(row)]
sorted_words_set = [[] for M in range(row)]


# 단어의 길이에 맞게 단어를 추가
for i in range(num_of_words):
    sorted_words[len(words[i]) - 1].append(words[i])

# 중복제거
for i in range(row):
    sorted_words_set[i] = set(sorted_words[i])
    sorted_words[i] = list(sorted_words_set[i])

# 정렬
for i in range(row):
    sorted_words[i].sort()

# 출력
for i in range(len(sorted_words)):
    for j in range(len(sorted_words[i])):
        print(sorted_words[i][j])