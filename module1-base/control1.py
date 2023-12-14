import string
from collections import Counter
import re
text = input()
words = text.split()
unique_words = set()

for word in words:
    # word = word.translate(str.maketrans("", "", string.punctuation))
    # word = word.lower()
    words = [re.sub(r'[!.,?;:#$%^&*()]+', '', word.lower()) for word in words]

    filtered_words = [word for word in words if len(word) >= 5 and len(set(word)) >= 4]

    # Получаем количество повторений каждого слова
    word_counts = Counter(filtered_words)

    # Отфильтровываем слова, которые встретились более 2х раз
    final_words = [word for word in word_counts if word_counts[word] > 2]

    # Сортируем слова в алфавитном порядке
final_words.sort()
for word in final_words:
    print(word)



#     unique_words.add(word)
#
# word_counts = {}
# for word in words:
#     if word in word_counts:
#         word_counts[word] += 1
#     else:
#         word_counts[word] = 1
#
# valid_words = []
# for word in unique_words:
#     if len(word) >= 5 and len(set(word)) >= 4 and word_counts[word] >= 2:
#         valid_words.append(word)
#
# valid_words = sorted(valid_words)
# print(valid_words)
# # for words in valid_words:
# #     print(words)