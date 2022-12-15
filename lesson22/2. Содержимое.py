# Выберите любую директорию на своём диске и затем напишите программу,
# выводящую на экран абсолютные пути к файлам и папкам, которые находятся внутри этой директории.
#
# Результат программы на примере директории проекта python_basic:
# Содержимое каталога G:\PycharmProjects\python_basic
#     G:\PycharmProjects\python_basic\.git
#     G:\PycharmProjects\python_basic\.idea
#     G:\PycharmProjects\python_basic\Module14
import os


def print_dirs(project):
    print('Содержимое директории', project)
    if os.path.exists(project):
        for i_elem in os.listdir(project):
            path = os.path.join(project, i_elem)
            print('    ', path)
    else:
        print('Каталога проекта не существует.')

folder_name = 'lesson18'

abs_path = os.path.abspath(os.path.join('..', folder_name))


print_dirs(abs_path)



# решение от курса:
# for path in os.listdir('..'):
#     print(os.path.join(os.path.abspath('..'), path))