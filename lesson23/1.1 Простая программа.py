# Напишите программу, которая открывает файл и записывает туда введённую пользователем строку.
# Используйте операторы try except else finally. Обработайте возможные ошибки:
#
# Проблема при открытии файла.
# Нельзя преобразовать данные в целое.
# Неожиданная ошибка.
test_file = None

try:
    test_file = open('test.txt', 'w', encoding='utf8')
    test_file.write(input('Введите текст: '))
except (TypeError, ValueError) as exc:
    print(exc, 'Нашлась ошибка')
else:
    print('Программа выполнилась без ошибок')
finally:
    test_file.close()
    print(test_file.closed)
