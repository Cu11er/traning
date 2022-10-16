# Пользователь вводит список из N чисел и число K.
# Напишите код, выводящий на экран сумму индексов элементов списка, которые кратны K.

numbers_count = int(input('Введите кол-во чисел: '))
numbers = []

for number in range(numbers_count):
    print('Введите', number + 1, 'число: ', end = '')
    number_input = int(input())
    numbers.append(number_input)

divider = int(input('Введите делитель: '))

sum_index = 0
for n in numbers:
    if n % divider == 0:
        print('Индекс числа', n, ':', numbers.index(n) )
        sum_index += numbers.index(n)
print('Сумма индексов:', sum_index)




