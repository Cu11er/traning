# В базе данных одной компании есть баг (или, может быть, фича): если ввести туда имя сотрудника меньше чем из трёх букв
# то база сломается и упадёт. Как компания принимает на работу людей, например, с китайскими именами, непонятно.
#
# Дан файл people.txt, в котором построчно хранится N имён пользователей.
#
# Напишите программу, которая берёт количество символов в каждой строке файла и в качестве ответа выводит общую сумму.
# Если в какой-либо строке меньше трёх символов (не считая литерала \n), то вызывается ошибка, и программа завершается.

names_file = open('people.txt', 'r')
sum_sym = 0
number_line = 0
try:
    for line in names_file:
        length = len(line)
        number_line += 1
        if line.endswith('\n'):
            length -= 1
        if length < 3:
            print('Имя короче 3 символов')
            raise BaseException
        else:
            sum_sym += length
    names_file.close()
except ValueError as exc:
    print(type(exc), 'Ошибка значения')
except BaseException as exc:
    print('Длина строки {} меньше 3 символов!'.format(number_line))

print('Сумма символов:', sum_sym)


# решение от курса
# peoples = open('people.txt', 'r', encoding='utf8')
# result = 0
# for line in peoples:
#     clear_line_len = len(line.rstrip())   # вернет копию строки str с удаленными символами chars в конце строки
#     result += clear_line_len
#     if clear_line_len < 3:
#         raise Exception
#
# print(result)