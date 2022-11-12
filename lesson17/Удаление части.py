# Дан список из N чисел, а также числа А и В (можно сгенерировать случайно, при этом А < B).
# Напишите программу, которая удаляет элементы списка с индексами от А до В.
# Не используйте дополнительные переменные и методы списков.

import random

numbers = [random.randint(1, 10) for _ in range(random.randint(5, 10))]
a = random.randint(0, len(numbers) - 2)
b = random.randint(a + 1, len(numbers) - 1)

print('Список', numbers, 'Удаляем элементы с индексами от', a, 'до', b)
numbers[a:b + 1] = []

print(numbers)
