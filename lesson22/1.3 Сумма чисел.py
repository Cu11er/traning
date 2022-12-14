# Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке.
# Напишите программу, которая выводит их сумму в выходной файл answer.txt.
#
# Пример:
# Содержимое файла numbers.txt:
# 1
# 2
# 3
# 4
# 10
#
# Содержимое файла answer.txt
# 20

numbers = open('numbers.txt', 'r')
count = 0
for strin in numbers:
    count += int(strin)
print(count)
numbers.close()
result = open('answer.txt', 'a')
result.write(str(count))
result.close()
