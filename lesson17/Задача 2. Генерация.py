# Пользователь вводит целое число N. Напишите программу, которая генерирует список из N чисел,
# на чётных местах в нём стоят единицы, а на нечётных — числа, равные остатку от деления своего номера на 5.
#
# Пример:
# Введите длину списка: 10
# Результат: [1, 1, 1, 3, 1, 0, 1, 2, 1, 4]
# numbers = [1 if num % 2 == 0 else num % 5 for num in range(len_numbers)]
#  если индекс числа четный, то равен 1, иначе индекс числа % 5 в длине списка 1, 10

len_numbers = int(input('Введите длину списка: '))
numbers = [1 if num % 2 == 0
           else num % 5
           for num in range(len_numbers)]

print(numbers)
