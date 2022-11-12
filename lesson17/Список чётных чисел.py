# user_list = [int(input('Введи число: ')) for _ in range(2)]

start = int(input('Левая граница: '))
stop = int(input('Правая граница: '))

result = [i_num for i_num in range(start, stop + 1) if i_num % 2 == 0]

print(result)
