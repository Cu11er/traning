# Друг никак не может понять эту тему с изменяемыми и неизменяемыми типами, ссылками, объектами и их id.
# Видя, как он мучается, вы решили помочь ему и объяснить эту тему наглядно.
# Пользователь вводит любой объект. Напишите программу, которая выводит на экран тип введённых данных,
# информацию о его изменяемости, а также id этого объекта.
#
# Пример 1:
# Введите данные: привет
#
# Тип данных: str (строка)
# Неизменяемый (immutable)
# Id объекта: 1705156583984
#
# Пример 2:
# Введите данные: {‘a’: 10, ‘b’: 20}
#
# Тип данных: dict (словарь)
# Изменяемый (mutable)
# Id объекта: 1705205308536

# if type(data) in (int, float, str, tuple, bool):
#     print('Неизменяемый (immutable)')
# elif type(data) in (str, set, dict):
#     print('Изменяемый (mutable)')
data_names_dict = {
    "<class 'str'>": "строка",
    "<class 'dict'>": "словарь",
    "<class 'list'>": "список",
    "<class 'set'>": "множество",
    "<class 'int'>": 'число',
    "<class 'bool'>": 'булево'
}

mutable_check_helper = {
    "mutable": ("словарь(dict)", "список(list)", "множество(set)"),
    "immutable": ("число(int)", "число с плавающей точкой(float)", "строка(str)", "кортеж(tuple)", "булево(bool)")
}


def check_info(data):
    type_of_data = type(data)
    name_of_data = ""
    if str(type_of_data) in data_names_dict:
        name_of_data = data_names_dict[str(type_of_data)]

    if name_of_data in mutable_check_helper["mutable"]:
        property_of_data = "Изменяемый (mutable)"
    else:
        property_of_data = "Неизменяемый (immutable)"

    print(f"Тип данных: {type_of_data} ({name_of_data})")
    print(property_of_data)
    print("Id объекта:", id(data))


data_in = True
check_info(data_in)
