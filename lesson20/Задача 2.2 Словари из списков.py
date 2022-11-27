# Создайте два списка, в каждом из которых лежит 10 случайных букв алфавита (могут повторяться).
# Затем для каждого списка создайте словарь из пар «индекс — значение» и выведите оба словаря на экран.
#
# Подсказка: random
#
# Пример:
# Первый список: ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
# Второй список: ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']
#
# Первый словарь: {0: 'й', 1: 'р', 2: 'с', 3: 'г', 4: 'а', 5: 'а', 6: 'т', 7: 'ж', 8: 'е', 9: 'к'}
# Второй словарь: {0: 'д', 1: 'а', 2: 'а', 3: 'в', 4: 'т', 5: 'ж', 6: 'р', 7: 'б', 8: 'й', 9: 'р'}

import random

def random_generator (symb, how_symb):
    result = list()
    for i in range(how_symb):
        result.append(random.choice(symb))
    return result


def get_index(text):
    result = dict()
    for index, sym in enumerate(text):
        result.update({index: sym})
    return result


symb = (
    'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
    'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
)

first_list = random_generator(symb, 10)
second_list = random_generator(symb, 10)
first_tuple = get_index(first_list)
second_tuple = get_index(second_list)

print('Первый список:', first_list)
print('Второй список:', second_list)
print('\nПервый словарь:', first_tuple)
print('Второй словарь:', second_tuple)
