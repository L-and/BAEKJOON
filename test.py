num_of_words = int(input())

words = list()

for i in range(num_of_words):
    word = input()
    words.append(word)

words.sort()

print(words)