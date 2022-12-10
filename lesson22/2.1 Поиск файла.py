# В уроке мы написали функцию, которая ищет нужный нам файл во всех подкаталогах указанной директории.
# Однако, как мы понимаем, файлов с таким названием может быть несколько.
# Напишите функцию, которая принимает на вход абсолютный путь до директории и имя файла,
# проходит по всем вложенным файлам и папкам и выводит на экран все абсолютные пути с этим именем.
#
# Пример:
# Ищем в: C:/Users/Roman/PycharmProjects/Skillbox
# Имя файла: lesson2
#
# Найдены следующие пути:
# C:/Users/Roman/PycharmProjects/Skillbox\Module15\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module16\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module17\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module18\lesson2.py
import os

def search_file(dir, file):
    # print('переходим', dir)
    for i_elem in os.listdir(dir):
        path = os.path.join(dir, i_elem)
        # print(path)
        if i_elem == file:
            print(os.path.abspath(path))

        if os.path.isdir(path):
            result = search_file(path, file)
            if result:
                break



file_name = 'Задача 1. Склады.py'  # что ищем
abs_path = os.path.abspath(os.path.join('..'))  # где ищем

print('Найдены следующие пути:')
search_file(abs_path, file_name)