num_of_words = int(input())

words = dict()

for i in range(num_of_words):
    word = input()
    words[word] = len(word)

words = dict(sorted(words.items(), key = lambda x : x[1]))

last_value = 0
last_key = str()
temp_list = list()

print(words.keys())

for key, value in words.items():
    if last_value == value:
        temp_list.append(last_key) 
    elif len(temp_list) != 0 and len(last_key) == len(temp_list[-1]):
        temp_list.append(key)

    last_value = value
    last_key = key

print(temp_list)
