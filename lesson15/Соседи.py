# Дана строка S и номер позиции символа в строке.
# Напишите программу, которая выводит соседей этого символа и сообщение о количестве таких же символов
# среди этих соседей: их нет, есть ровно один или есть два таких же.

user_str = input('Введите строку: ') # abcd
user_index = int(input('Номер символа: ')) - 1

user_str = list(user_str)
count = 0
if user_index > 0:
    print('Символ слева:', user_str[user_index - 1])
    if user_str[user_index - 1] == user_str[user_index]:
        count += 1
if user_index < len(user_str)-1:
    print('Символ справа:', user_str[user_index + 1])
    if user_str[user_index + 1] == user_str[user_index]:
        count += 1

if count == 2:
     print('Рядом есть два таких же символа')
elif count == 1:
    print('Рядом есть такойже символ')
elif count == 0:
    print('Рядом таких же символов нет')
