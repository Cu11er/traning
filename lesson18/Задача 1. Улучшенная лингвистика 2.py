# Задача 1. Улучшенная лингвистика 2
# Усовершенствуйте старую программу:
# У нас есть список из трёх слов, которые вводит пользователь. Затем вводится сам текст произведения,
# который вводится уже в одну строку. Напишите программу, которая посчитает,
# сколько раз слова пользователя встречаются в тексте.

# count = [0, 0, 0]
# user_input = input('Введите три слова через пробел: ')
# user_words = user_input.split()
# words = input('Введите текст произведения: ')
# words_list = words.split()
#
# for index in range(3):
#     for word in words_list:
#         if user_words[index] == word:
#             count[index] += 1
#
# print('Подсчет слов в тексте:\n')
# for i in range(3):
#     print(user_words[i], ':', count[i])

# как надо было сделать
words = [input("Введите слово: ") for _ in range(3)]
text = input("Введите текст: ")
words_count = [text.count(word) for word in words]

print(words_count)
