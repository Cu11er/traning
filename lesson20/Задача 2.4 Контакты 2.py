# Мы уже реализовывали телефонную книгу для Степана, однако её проблема была в том,
# что туда нельзя было добавить людей с одинаковыми именами. Надо это исправить.
#
# Напишите программу, которая запрашивает у пользователя имя контакта, фамилию и номер телефона,
# добавляет их в словарь и выводит на экран текущий словарь контактов. Словарь состоит из пар «Ф. И. — телефон»,
# где Ф. И. — это составной ключ. Запрос на добавление идёт бесконечно
# (но можно задать своё условие для завершения программы).
# Обеспечьте контроль ввода: если этот человек уже есть в словаре, то выведите соответствующее сообщение.

def print_phonebook(data):
    print('\nТелефонная книга:')
    for user in data:
        print(f'{user[0]} {user[1]}: {data[user]}')

phonebook = dict()
while True:
    first_name = input('\nВведите фамилию ("выход" чтобы закончить): ')
    if first_name != 'выход':
        second_name = input('Введите имя: ')
        contact = (first_name, second_name)
        user_number = int(input('Введите номер телефона: '))
        if contact not in phonebook:
            phonebook.update({contact: user_number})
            print_phonebook(phonebook)
        else:
            print('Такой контакт уже есть!')
    else:
        break

# решение от курса:
# contacts = {}
#
# while True:
#     name = input("Введите имя: ")
#     surname = input("Введите фамилию: ")
#     name_n_surname = (name, surname)
#     if name_n_surname not in contacts:
#         contacts[name_n_surname] = int(input("Введите номер телефона: "))
#     else:
#         print("Такой контакт уже есть!")
#     print(contacts)
