# Задача 3. IP-адрес
# IP-адрес компьютера состоит из 4 чисел, разделённых точкой. Каждое число находится в диапазоне от 0 до 255 (включительно).
#
# Пример правильного адреса: 192.168.1.0
# Пример неправильного адреса: 192.168.300.0
#
# Напишите программу, которая получает на вход 4 числа и выводит на экран IP-адрес.
# Используйте переменную ip_address в качестве шаблона. Обеспечьте контроль ввода.

# for num in range(4):
#     ip_address = ''
#     print('Ведите число: ')
#     num1 = int(input())
#     if num1 > 255:
#         print('Число не может быть больше "255"')
#         num = int(input())
#
#     num += 1
# print(ip_address)

ip_address = '{0}.{1}.{2}.{3}'
count = 0
numbers = []
while count < 4:
    new_number = int(input('Введите число:'))
    if 0 < new_number <= 255:
        numbers.append(new_number)
        count += 1
    else:
        print('Ошибка ввода! Цифра не может быть больше "255"')

print(ip_address.format(numbers[0], numbers[1], numbers[2], numbers[3]))
