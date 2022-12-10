# Напишите программу, которая выводит на экран только корень диска, на котором запущен скрипт.
# Учтите, что скрипт может быть запущен где угодно и при любой вложенности папок.
#
# Результат программы на примере диска G:
# Корень диска: G:\\

import os


def print_dirs(project):
    for i_elem in os.listdir(project):
        path = os.path.join(project, i_elem)
        print(' ', path)

abs_path = os.path.abspath(os.path.join(os.path.sep))
print('Содержимое каталога', abs_path)
print_dirs(abs_path)

