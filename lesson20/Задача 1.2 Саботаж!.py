# Какой-то нехороший человек решил подпортить жизнь frontend-разработчикам и добавил в код сайта символ ~ (тильда).
# Но программисты быстро решили эту проблему, пройдясь по всему коду маленькой программой.
#
# Пользователь вводит строку. Напишите программу, которая проходит по строке и выводит в консоль индексы символа ~.
# Для решения этой задачи (и остальных тоже) используйте функцию enumerate.
#
# Пример:
# Строка: so~mec~od~e
# Ответ: 2 6 9

str_input = input('Строка:')

for i_sym, sym in enumerate(str_input):
    if sym == '~':
        print(i_sym, end=' ')

# решение с list comprehension
result = [str(i_sym) for i_sym, sym in enumerate(str_input) if sym == '~']
print(('Ответ:'), ' '.join(result))

# решение с использованием функции (выводим индекс необходимого символа)
def get_indexes(where_to_search, what_to_search):
    return [str(index) for index, letter in enumerate(where_to_search) if letter == what_to_search]

# генератор кортежа из случайных чисел
def create_random_tuple(a, b, n):
    return tuple([random.randint(a, b) for _ in range(n)])
#  first = create_random_tuple(0, 5, 10) - создать кортеж из 10 случайных чисел от 0 до 5

print(('Ответ:'), ' '.join(get_indexes(str_input, '~')))
