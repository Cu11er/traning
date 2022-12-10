# Одному программисту дали задачу для обработки неких результатов тестирования двух групп людей.
# Файл первой группы (group_1.txt) находится в папке task, файл второй группы (group_2.txt) — в папке Additional_info.
# Содержимое файла group_1.txt
# Бобровский Игорь 10
# Дронов Александр 20
# Жуков Виктор 30
#
# Содержимое файла group_2.txt
# Павленко Геннадий 20
# Щербаков Владимир 35
# Marley Bob 15
#
# На экран нужно было вывести сумму очков первой группы, затем разность очков опять же первой группы
# и напоследок — произведение очков уже второй группы.
# Программист оказался не очень опытным, писал код наобум и даже не стал его проверять. И оказалось,
# этот код просто не работает. Вот что он написал:
# file = open('E:\task\group_1.txt', 'read')
# summa = 0
# for i_line in file:
#     info = i_line.split()
#     summa += info[2]
# file = open('E:\task\group_1.txt', 'read')
# diff = 0
# for i_line in file:
#     info = i_line.split()
#     diff -= info[2]
# file_2 = open('E:\task\group_2.txt', 'read')
# compose = 0
# for i_line in file:
#     info = i_line.split()
#     compose *= info[2]
# print(summa)
# print(diff)
# print(compose)
#
# Исправьте код для решения поставленной задачи. Для проверки результата создайте необходимые папки
# (task, Additional_info, Dont touch me) на своём диске в соответствии с картинкой и также добавьте файлы
# group_1.txt и group_2.txt.
import os

print(os.listdir())
file = open('F:\\task\\group_1.txt', 'r', encoding='utf-8')

summa = 0
diff = 0
for i_line in file:
    info = i_line.split('\n')
    info = info[0].split(' ')
    summa += int(info[2])
    diff -= int(info[2])
file.close()

file_2 = open('F:\\task\\Additional_info\\group_2.txt', 'r', encoding='utf-8')
compose = 1
for i_line_2 in file_2:
    info_2 = i_line_2.split('\n')
    info_2 = info_2[0].split(' ')
    compose *= int(info_2[2])
    print(info_2[2])
file_2.close()

print(summa)
print(diff)
print(compose)
