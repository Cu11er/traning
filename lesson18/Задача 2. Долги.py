# Задача 2. Долги
# Один наш друг занял у нас определённую сумму денег и всё никак не может их вернуть.
# А деньги нам нужны. Поэтому мы решили написать небольшой скрипт-напоминалку, который, возможно, разбудит его совесть.
#
# Напишите программу, которая получает на вход имя и долг, а затем выводит на экран сообщение,
# где имя повторяется несколько раз (и долг, возможно, тоже). Используйте числа в названиях ключей.
#
# Пример:
# Введите имя: Том
# Введите долг: 100
# Том! Том, привет! Как дела, Том? Где мои 100 рублей? Том!


user_name = input('Введите имя: ')
user_debt = int(input('Введите долг: '))

print('{0}! {0}, привет! Как дела, {0}? Где мои бабки, '
      '{0}? Когда вернешь {1} рублей, пёс?'.format(user_name, user_debt))
