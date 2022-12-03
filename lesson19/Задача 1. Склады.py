# У мебельного магазина есть два склада, на которых хранятся разные категории товаров по парам «название — количество»:
#
# small_storage = {
#     'гвозди': 5000,
#     'шурупы': 3040,
#     'саморезы': 2000
# }
#
# big_storage = {
#     'доски': 1000,
#     'балки': 150,
#     'рейки': 600
# }
#
# Магазин решил сократить аренду и скинуть все товары в большой склад (big_storage). После этого нас попросили реализовать поиск по товарам.
# Напишите программу, которая объединяет оба словаря в один (в big_storage), затем запрашивает у пользователя название товара и выводит
# на экран его количество. Если такого товара нет, то выводит об этом ошибку. Для получения значения используйте метод get.

small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)

while True:
    input_item = input('Введите название товара: ')
    for item in big_storage.keys():
        if item == input_item:
            print('Количество товара', item, '-', big_storage.get(item))
            break
    else:
        print('Ошибка! Такого товара в базе нет!')


# решение от курса:
# big_storage.update(small_storage)
#
# user_item = input("Введите название нужного товара: ")
# if big_storage.get(user_item, None):
#     print(big_storage[user_item])
# else:
#     print("Такого товара нет!")
