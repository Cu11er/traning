# Задача 2. Сервер
# У вас есть данные о сервере, которые хранятся в виде вот такого словаря:
## server_data = {
#     "server": {
#         "host": "127.0.0.1",
#         "port": "10"
#     },
#     "configuration": {
#         "access": "true",
#         "login": "Ivan",
#         "password": "qwerty"
#     }
# }
## Напишите программу, которая выводит для пользователя эти данные так же красиво и понятно, как они представлены в словаре.
# Результат работы программы:
# server:
#     host: 127.0.0.1
#     port: 10
# configuration:
#     access: true
#     login: Ivan
#     password: qwerty

server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for i_keys, i_values in server_data.items():
    print('{key}:'.format(key=i_keys), end='\n')
    for j_keys, j_values in i_values.items():  # вместо "server_data[i_keys].items()" можно обратится напрямую к значению
        print('\t{j_keys}: {j_values}'.format(j_keys=j_keys, j_values=j_values))

