# Задача 1. Гласные буквы
# Что нужно сделать
#
# Команде лингвистов понравилось качество ваших программ, и они решили заказать у вас функцию для анализатора текста,
# которая создавала бы список гласных букв текста, а заодно считала бы их количество.
# Напишите программу, которая запрашивает у пользователя текст и генерирует список из гласных букв этого текста
# (сама строка вводится на русском языке). Выведите в консоль сам список и его длину.
#
# Пример:
# Введите текст: Нужно отнести кольцо в Мордор!
#
# Список гласных букв: ['у', 'о', 'о', 'е', 'и', 'о', 'о', 'о', 'о']
# Длина списка: 9

def vowels(words):
    words_list = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е', 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е']
    result = [i_words for i_words in words if i_words in words_list] #  символ для символа в тексте (words) если
                                                                     # символ встречается в списке (words_list) то добавить в список result
    return result


words = [word for word in input('Введите текст: ')]
print(vowels(words))
