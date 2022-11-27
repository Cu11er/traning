# Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно.
# Также заполните второй кортеж числами от −5 до 0. Объедините два кортежа, создав тем самым третий кортеж.
# С помощью метода кортежа определите в нём количество нулей. Выведите на экран третий кортеж и количество нулей в нём.
words = ('нулей', 'ноль', 'нуля', 'нуля', 'нуля', 'нулей', 'нулей', 'нулей', 'нулей', 'нулей', 'нулей')

import random

numbers = (0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5)
negative_numbers = (-5, -4, -3, -2, -1, 0, -5, -4, -3, -2, -1, 0,)
one_tuple = tuple(random.sample(numbers, 10))
two_tuple = tuple(random.sample(negative_numbers, 10))
result_tuple = one_tuple + two_tuple

print('Первый кортеж', one_tuple)
print('Второй кортеж', two_tuple)
print('Третий кортеж {} \nв нем: {} {}'.format(result_tuple, result_tuple.count(0), words[result_tuple.count(0)]))
