# Вы работаете системным администратором в одной компании. На диске каждого сотрудника компании
# в специальной папке access лежит файл admin.bat. Этот файл предназначен для вас, и вам нужен путь до этого файла,
# причём как относительный, так и абсолютный. Недолго думая, вы решили написать небольшой скрипт,
# который закинете по сети к этому файлу.
# Напишите программу, которая выводит на экран относительный и абсолютный пути до файла admin.bat.
#
# Пример результата:
# Абсолютный путь до файла: C:\Users\Roman\PycharmProjects\Skillbox\access\admin.bat
# Относительный путь до файла: Skillbox\access\admin.bat
import os


folder_name = 'access'
file_name = 'admin.bat'
rel_path = os.path.join('Skillbox', folder_name, file_name)
abs_path = os.path.abspath(rel_path)

print('Относительный путь до файла:', rel_path)
print('Абсолютный путь до файла:', abs_path)
